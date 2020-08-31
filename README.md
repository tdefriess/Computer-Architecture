# LS8 Emulator

This is a week long project I did as a part of the Lambda School Computer Science curriculum.

This project emulates an 8-bit computer which may accept assembly code from the .ls8 files and run them in the terminal. This emulator simulates RAM reads, writes, and the use of a system stack written to RAM. The program begins by reading a program from an .ls8 file into RAM starting from index 0. After initialization, the emulator reads from RAM three indexes at a time, using the first input to determine which actions to perform and how to update the Program Counter, which is the pointer that tracks the currently executing instruction. I have implemented all ALU operations, including bitwise operations, per the spec.
