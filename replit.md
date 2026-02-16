# CalcHub - Professional Calculator Tools Hub

## Overview
A static HTML website providing various calculator tools (BMI, EMI, GPA, Tip, Age, Compound Interest, Percentage, AdSense Revenue). No build system or backend required.

## Project Architecture
- Static HTML files served via Python's built-in HTTP server
- `server.py` - Simple HTTP server on port 5000 with cache-control headers
- `index.html` - Homepage
- `tools/` - Individual calculator tool pages
- `_next/static/` - CSS, JS chunks, and media assets
- Other pages: about, contact, privacy, terms, disclaimer

## Running
- Workflow "Start application" runs `python server.py` on port 5000
