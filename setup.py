#!/usr/bin/env python3
"""
Smart CCTV System - Quick Start Guide
"""

import os
import subprocess
import sys

def setup_project():
    """Setup the Smart CCTV System project."""
    print("=" * 60)
    print("Smart CCTV System - Setup")
    print("=" * 60)
    
    # Check Python version
    print("\n✓ Checking Python version...")
    if sys.version_info < (3, 8):
        print("✗ Python 3.8+ is required")
        sys.exit(1)
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Check if .env exists
    print("\n✓ Checking configuration...")
    if not os.path.exists('.env'):
        print("ℹ Creating .env from .env.example...")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as src:
                with open('.env', 'w') as dst:
                    dst.write(src.read())
            print("✓ .env created")
        else:
            print("✗ .env.example not found")
    else:
        print("✓ .env already exists")
    
    # Create necessary directories
    print("\n✓ Setting up directories...")
    directories = ['logs', 'recordings', 'data']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✓ {directory}/")
    
    # Check dependencies
    print("\n✓ Checking dependencies...")
    try:
        import cv2
        import flask
        import numpy
        print("✓ All required packages found")
    except ImportError:
        print("✗ Some packages are missing")
        print("\nInstalling dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Edit .env file with your camera settings")
    print("2. Run: python main.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\nFor more information, see README.md")

if __name__ == '__main__':
    setup_project()
