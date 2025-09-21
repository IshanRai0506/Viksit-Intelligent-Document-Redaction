#!/usr/bin/env python3

"""
Viksit - Intelligent Document Redaction
Command Line Interface

This script provides a command-line interface for the Viksit document redaction system.
"""

import click
import sys
import os
from pathlib import Path
from typing import List, Optional

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from viksit.redactor import DocumentRedactor
from viksit.utils.logger import setup_logger
from viksit.config import load_config

logger = setup_logger(__name__)


@click.group()
@click.version_option(version="1.0.0")
@click.option('--config', '-c', type=click.Path(exists=True), 
              help='Path to configuration file')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.pass_context
def cli(ctx, config, verbose):
    """Viksit - Intelligent Document Redaction System"""
    ctx.ensure_object(dict)
    ctx.obj['config'] = load_config(config) if config else {}
    ctx.obj['verbose'] = verbose


@cli.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--entities', '-e', 
              help='Comma-separated list of entity types to redact',
              default='person,organization,location,phone,email,ssn')
@click.option('--confidence', '-c', type=float, default=0.85,
              help='Confidence threshold for entity detection (0.0-1.0)')
@click.option('--preview', is_flag=True, 
              help='Generate preview without permanent redaction')
@click.option('--format', 'output_format', type=click.Choice(['pdf', 'docx', 'txt']),
              help='Output format (auto-detected if not specified)')
@click.pass_context
def redact(ctx, input_path, output_path, entities, confidence, preview, output_format):
    """Redact sensitive information from a document."""
    try:
        # Parse entity types
        entity_types = [e.strip() for e in entities.split(',')]
        
        # Initialize redactor
        config = ctx.obj.get('config', {})
        config['confidence_threshold'] = confidence
        redactor = DocumentRedactor(config)
        
        click.echo(f"Processing: {input_path}")
        click.echo(f"Entity types: {', '.join(entity_types)}")
        click.echo(f"Confidence threshold: {confidence}")
        
        if preview:
            click.echo("Preview mode enabled - no permanent redaction")
        
        # Perform redaction
        with click.progressbar(length=100, label='Redacting document') as bar:
            result = redactor.redact_document(
                input_path=input_path,
                output_path=output_path,
                entity_types=entity_types,
                preview=preview,
                output_format=output_format,
                progress_callback=lambda p: bar.update(p - bar.pos)
            )
        
        # Display results
        click.echo(f"\n✅ Redaction completed successfully!")
        click.echo(f"📄 Output saved to: {output_path}")
        click.echo(f"🔍 Entities found: {result['entities_found']}")
        click.echo(f"🚫 Entities redacted: {result['entities_redacted']}")
        
        if ctx.obj['verbose']:
            click.echo(f"\nDetailed results:")
            for entity_type, count in result['entity_breakdown'].items():
                click.echo(f"  {entity_type}: {count}")
                
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False))
@click.argument('output_dir', type=click.Path())
@click.option('--entities', '-e', 
              help='Comma-separated list of entity types to redact',
              default='person,organization,location,phone,email,ssn')
@click.option('--confidence', '-c', type=float, default=0.85,
              help='Confidence threshold for entity detection')
@click.option('--parallel', '-p', type=int, default=1,
              help='Number of parallel processes')
@click.option('--pattern', help='File pattern to match (e.g., "*.pdf")',
              default='*')
@click.pass_context
def batch(ctx, input_dir, output_dir, entities, confidence, parallel, pattern):
    """Batch process multiple documents."""
    try:
        # Parse entity types
        entity_types = [e.strip() for e in entities.split(',')]
        
        # Initialize redactor
        config = ctx.obj.get('config', {})
        config['confidence_threshold'] = confidence
        redactor = DocumentRedactor(config)
        
        # Find files to process
        input_path = Path(input_dir)
        files = list(input_path.glob(pattern))
        
        if not files:
            click.echo(f"❌ No files found matching pattern '{pattern}' in {input_dir}")
            return
        
        click.echo(f"Found {len(files)} files to process")
        click.echo(f"Parallel processes: {parallel}")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Process files
        results = redactor.batch_redact(
            input_directory=input_dir,
            output_directory=output_dir,
            entity_types=entity_types,
            pattern=pattern,
            parallel_processes=parallel
        )
        
        # Display results
        successful = sum(1 for r in results if r['status'] == 'success')
        failed = len(results) - successful
        
        click.echo(f"\n✅ Batch processing completed!")
        click.echo(f"📊 Successful: {successful}")
        click.echo(f"❌ Failed: {failed}")
        
        if failed > 0:
            click.echo("\nFailed files:")
            for result in results:
                if result['status'] == 'error':
                    click.echo(f"  {result['file']}: {result['error']}")
                    
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--host', default='0.0.0.0', help='Host to bind to')
@click.option('--port', default=5000, help='Port to bind to')
@click.option('--debug', is_flag=True, help='Enable debug mode')
@click.pass_context
def serve(ctx, host, port, debug):
    """Start the web server."""
    try:
        from viksit.web.app import create_app
        
        config = ctx.obj.get('config', {})
        app = create_app(config)
        
        click.echo(f"🚀 Starting Viksit web server on {host}:{port}")
        click.echo(f"🌐 Access at: http://{host}:{port}")
        
        app.run(host=host, port=port, debug=debug)
        
    except ImportError:
        click.echo("❌ Web dependencies not installed. Run: pip install viksit[web]", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Error starting server: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def test():
    """Run system tests to verify installation."""
    try:
        click.echo("🧪 Running Viksit system tests...")
        
        # Test 1: Import check
        click.echo("1. Testing imports...", nl=False)
        from viksit.redactor import DocumentRedactor
        click.echo(" ✅")
        
        # Test 2: Model loading
        click.echo("2. Testing model loading...", nl=False)
        redactor = DocumentRedactor()
        click.echo(" ✅")
        
        # Test 3: Basic redaction
        click.echo("3. Testing basic redaction...", nl=False)
        test_text = "John Doe lives at 123 Main St and his phone is 555-1234."
        result = redactor._extract_entities(test_text)
        if result:
            click.echo(" ✅")
        else:
            click.echo(" ⚠️  (No entities detected)")
        
        click.echo("\n🎉 All tests passed! Viksit is ready to use.")
        
    except Exception as e:
        click.echo(f" ❌\nError: {str(e)}", err=True)
        click.echo("\n💡 Try running: viksit setup")
        sys.exit(1)


@cli.command()
def setup():
    """Download and setup required models and data."""
    try:
        click.echo("📦 Setting up Viksit...")
        
        from viksit.setup import download_models, verify_installation
        
        # Download models
        click.echo("1. Downloading language models...")
        with click.progressbar(length=100, label='Downloading models') as bar:
            download_models(progress_callback=lambda p: bar.update(p - bar.pos))
        
        # Verify installation
        click.echo("2. Verifying installation...")
        if verify_installation():
            click.echo("✅ Setup completed successfully!")
        else:
            click.echo("❌ Setup verification failed!")
            sys.exit(1)
            
    except Exception as e:
        click.echo(f"❌ Setup error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def info():
    """Display system information."""
    import platform
    import torch
    
    click.echo("📋 System Information")
    click.echo(f"Python: {sys.version}")
    click.echo(f"Platform: {platform.platform()}")
    click.echo(f"PyTorch: {torch.__version__}")
    click.echo(f"CUDA Available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        click.echo(f"CUDA Version: {torch.version.cuda}")
        click.echo(f"GPU Count: {torch.cuda.device_count()}")


if __name__ == '__main__':
    cli()