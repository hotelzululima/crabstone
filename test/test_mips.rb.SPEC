****************
Platform: MIPS-32 (Big-endian)
Code:0x0c 0x10 0x00 0x97 0x00 0x00 0x00 0x00 0x24 0x02 0x00 0x0c 0x8f 0xa2 0x00 0x00 0x34 0x21 0x34 0x56 
Disasm:
0x1000:	jal	0x40025c
	op_count: 1
		operands[0].type: IMM = 0x40025c

0x1004:	nop	

0x1008:	addiu	$v0, $zero, 0xc
	op_count: 3
		operands[0].type: REG = v0
		operands[1].type: REG = zero
		operands[2].type: IMM = 0xc

0x100c:	lw	$v0, ($sp)
	op_count: 2
		operands[0].type: REG = v0
		operands[1].type: MEM
			operands[1].mem.base: REG = sp

0x1010:	ori	$at, $at, 0x3456
	op_count: 3
		operands[0].type: REG = at
		operands[1].type: REG = at
		operands[2].type: IMM = 0x3456

0x1014:

****************
Platform: MIPS-64-EL (Little-endian)
Code:0x56 0x34 0x21 0x34 0xc2 0x17 0x01 0x00 
Disasm:
0x1000:	ori	$at, $at, 0x3456
	op_count: 3
		operands[0].type: REG = at
		operands[1].type: REG = at
		operands[2].type: IMM = 0x3456

0x1004:	srl	$v0, $at, 0x1f
	op_count: 3
		operands[0].type: REG = v0
		operands[1].type: REG = at
		operands[2].type: IMM = 0x1f

0x1008:

****************
Platform: MIPS-32R6 | Micro (Big-endian)
Code:0x00 0x07 0x00 0x07 0x00 0x11 0x93 0x7c 0x01 0x8c 0x8b 0x7c 0x00 0xc7 0x48 0xd0 
Disasm:
0x1000:	break	7, 0
	op_count: 2
		operands[0].type: IMM = 0x7
		operands[1].type: IMM = 0x0

0x1004:	wait	0x11
	op_count: 1
		operands[0].type: IMM = 0x11

0x1008:	syscall	0x18c
	op_count: 1
		operands[0].type: IMM = 0x18c

0x100c:	rotrv	$t1, $a2, $a3
	op_count: 3
		operands[0].type: REG = t1
		operands[1].type: REG = a2
		operands[2].type: REG = a3

0x1010:

****************
Platform: MIPS-32R6 (Big-endian)
Code:0xec 0x80 0x00 0x19 0x7c 0x43 0x22 0xa0 
Disasm:
0x1000:	addiupc	$a0, 0x64
	op_count: 2
		operands[0].type: REG = a0
		operands[1].type: IMM = 0x64

0x1004:	align	$a0, $v0, $v1, 2
	op_count: 4
		operands[0].type: REG = a0
		operands[1].type: REG = v0
		operands[2].type: REG = v1
		operands[3].type: IMM = 0x2

0x1008:

