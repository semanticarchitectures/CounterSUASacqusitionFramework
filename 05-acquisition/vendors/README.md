# Vendor Repository

This directory contains profiles and capability data for C-sUAS hardware and software vendors.

## Structure

Each vendor should have a dedicated subdirectory (e.g., `vendor-name/`) with the following standard files:

- `profile.md`: General company information, contact details, and past performance.
- `capabilities.json`: Structured data defining performance parameters (ranges, modalities, Pk estimates).
- `contracts/`: Folder containing links or copies of specific task orders, NDAs, or funding alignments.

## Cross-Referencing

The `vendor_id` used in `capabilities.json` should match the identifiers used in T&E result reports located in `04-analysis/te-results/`.
