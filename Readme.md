# Lab: Code Generation Testing Guide

This guide explains how to compile KPL source files into binary format and verify the generated instructions using the `dump.py` tool.

## 1. Prerequisites
Before testing, ensure you have built the compiler in the `incompleted/` directory:
```bash
cd incompleted
make
cd ..
```

## 2. Testing Workflow

All testing commands should be executed inside the `tests/` directory:
```bash
cd tests
```

### Step 2.1: Generate Your Binary File
Compile the `.kpl` source code into a binary file. We use the `_bin` suffix to distinguish your output from the reference file.
```bash
..\incompleted\kplc <kpl_file> <bin_file>
..\incompleted\kplc example4.kpl example4_bin
```

### Step 2.2: Compare with Reference
Use `dump.py` to display the instructions (OpCodes) in the terminal. Compare your output with the provided reference binary.

*   **View Reference (The Goal):**
    ```bash
    python dump.py example4
    ```
*   **View Your Result (The Check):**
    ```bash
    python dump.py example4_bin
    ```