	.file	"client.yr"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$24, %rsp
	.cfi_offset 3, -24
	movl	%edi, -20(%rbp)
	movq	%rsi, -32(%rbp)
	movq	-32(%rbp), %rcx
	movl	-20(%rbp), %eax
	movl	$_Ymain, %edx
	movq	%rcx, %rsi
	movl	%eax, %edi
	call	y_run_main
	movl	%eax, %ebx
	movl	%ebx, %eax
	addq	$24, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.globl	_Y6client7printlnFNcxAyacxAyaZv
	.type	_Y6client7printlnFNcxAyacxAyaZv, @function
_Y6client7printlnFNcxAyacxAyaZv:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, %rax
	movq	%rsi, %rcx
	movq	%rcx, %rdx
	movq	%rax, -32(%rbp)
	movq	%rdx, -24(%rbp)
	movq	-32(%rbp), %rax
	movq	%rax, -16(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -8(%rbp)
	movq	-16(%rbp), %rdx
	movq	-8(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y4core2io5printFcxAyaZcv
	movl	$10, %edi
	call	_Y4core2io5printFaZcv
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	_Y6client7printlnFNcxAyacxAyaZv, .-_Y6client7printlnFNcxAyacxAyaZv
	.section	.rodata
.LC0:
	.string	"Usage :"
.LC1:
	.string	" client [ip_address port]"
	.align 8
.LC2:
	.string	"\n Without any ip address and port, the default values are 127.0.0.1 and 8888.\n"
	.text
	.globl	_Y6client10printUsageFZv
	.type	_Y6client10printUsageFZv, @function
_Y6client10printUsageFZv:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	$7, -16(%rbp)
	movq	$.LC0, -8(%rbp)
	movq	-16(%rbp), %rdx
	movq	-8(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
	movq	$25, -32(%rbp)
	movq	$.LC1, -24(%rbp)
	movq	-32(%rbp), %rdx
	movq	-24(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
	movq	$78, -48(%rbp)
	movq	$.LC2, -40(%rbp)
	movq	-48(%rbp), %rdx
	movq	-40(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	_Y6client10printUsageFZv, .-_Y6client10printUsageFZv
	.globl	_Y6client13isIntegralNtNFNcxtZcxb
	.type	_Y6client13isIntegralNtNFNcxtZcxb, @function
_Y6client13isIntegralNtNFNcxtZcxb:
.LFB3:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	.cfi_offset 3, -24
	movl	$1, %eax
	movl	%eax, %ebx
	movl	%ebx, %eax
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
	.size	_Y6client13isIntegralNtNFNcxtZcxb, .-_Y6client13isIntegralNtNFNcxtZcxb
	.globl	_Y6client5toNtNFNAyaAyaZcxt
	.type	_Y6client5toNtNFNAyaAyaZcxt, @function
_Y6client5toNtNFNAyaAyaZcxt:
.LFB4:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	.cfi_offset 3, -24
	movq	%rdi, %rax
	movq	%rsi, %rcx
	movq	%rcx, %rdx
	movq	%rax, -48(%rbp)
	movq	%rdx, -40(%rbp)
	movq	-40(%rbp), %rdx
	movq	-48(%rbp), %rax
	subq	$1, %rax
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	subl	$48, %eax
	movzbl	%al, %eax
	movw	%ax, -18(%rbp)
	movq	-48(%rbp), %rax
	subl	$2, %eax
	movl	%eax, -24(%rbp)
	movw	$10, -26(%rbp)
	jmp	.L14
.L15:
	nop
.L9:
	movq	-40(%rbp), %rdx
	movl	-24(%rbp), %eax
	cltq
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	subl	$48, %eax
	movzbl	%al, %eax
	imulw	-26(%rbp), %ax
	addw	%ax, -18(%rbp)
	movzwl	-26(%rbp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	addl	%eax, %eax
	movw	%ax, -26(%rbp)
	subl	$1, -24(%rbp)
.L14:
	nop
.L8:
	cmpl	$0, -24(%rbp)
	jns	.L15
	nop
.L11:
	movzwl	-18(%rbp), %eax
	movl	%eax, %ebx
	movl	%ebx, %eax
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE4:
	.size	_Y6client5toNtNFNAyaAyaZcxt, .-_Y6client5toNtNFNAyaAyaZcxt
	.section	.rodata
.LC3:
	.string	"127.0.0.1"
.LC4:
	.string	"Socket error"
.LC5:
	.string	"Connect error"
.LC6:
	.string	"Connected to server !"
	.text
	.globl	_Ymain
	.type	_Ymain, @function
_Ymain:
.LFB5:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$136, %rsp
	.cfi_offset 3, -24
	movq	%rdi, %rax
	movq	%rsi, %rcx
	movq	%rcx, %rdx
	movq	%rax, -144(%rbp)
	movq	%rdx, -136(%rbp)
	movl	$0, -20(%rbp)
	movw	$8888, -22(%rbp)
	movq	$9, -48(%rbp)
	movl	$9, %eax
	movq	%rax, %rdi
	call	GC_malloc
	movq	%rax, -40(%rbp)
	movl	$9, %edx
	movq	-40(%rbp), %rax
	movl	$.LC3, %esi
	movq	%rax, %rdi
	call	memcpy
	movq	-144(%rbp), %rax
	cmpq	$1, %rax
	jbe	.L33
	nop
.L18:
	movq	-144(%rbp), %rax
	cmpq	$3, %rax
	je	.L34
	nop
.L21:
	call	_Y6client10printUsageFZv
	movl	$1, %eax
	jmp	.L32
.L34:
	nop
.L22:
	movq	-136(%rbp), %rax
	addq	$16, %rax
	movq	8(%rax), %rdx
	movq	(%rax), %rax
	movq	%rax, -48(%rbp)
	movq	%rdx, -40(%rbp)
	movq	-136(%rbp), %rax
	addq	$32, %rax
	movq	(%rax), %rdx
	movq	8(%rax), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client5toNtNFNAyaAyaZcxt
	movw	%ax, -22(%rbp)
.L33:
	nop
.L19:
	movl	$0, %edx
	movl	$1, %esi
	movl	$2, %edi
	call	socket
	movl	%eax, -28(%rbp)
	cmpl	$0, -28(%rbp)
	jns	.L35
	nop
.L25:
	movq	$12, -64(%rbp)
	movq	$.LC4, -56(%rbp)
	movq	-64(%rbp), %rdx
	movq	-56(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
	movl	$-1, %eax
	nop
	jmp	.L32
.L35:
	nop
.L26:
	leaq	-96(%rbp), %rax
	movl	$16, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	memset
	movq	-96(%rbp), %rax
	movq	-88(%rbp), %rdx
	movq	%rax, -80(%rbp)
	movq	%rdx, -72(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, %rdi
	call	inet_addr
	movl	%eax, -76(%rbp)
	movw	$2, -80(%rbp)
	movzwl	-22(%rbp), %eax
	movl	%eax, %edi
	call	htons
	movw	%ax, -78(%rbp)
	leaq	-80(%rbp), %rax
	movl	-28(%rbp), %ecx
	movl	$16, %edx
	movq	%rax, %rsi
	movl	%ecx, %edi
	call	connect
	testl	%eax, %eax
	jns	.L36
	nop
.L28:
	movq	$13, -112(%rbp)
	movq	$.LC5, -104(%rbp)
	movq	-112(%rbp), %rdx
	movq	-104(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
	movl	$-1, -20(%rbp)
	jmp	.L37
.L36:
	nop
.L29:
	movq	$21, -128(%rbp)
	movq	$.LC6, -120(%rbp)
	movq	-128(%rbp), %rdx
	movq	-120(%rbp), %rax
	movq	%rdx, %rdi
	movq	%rax, %rsi
	call	_Y6client7printlnFNcxAyacxAyaZv
.L37:
	nop
.L30:
	nop
.L31:
	movl	-28(%rbp), %eax
	movl	%eax, %edi
	call	close
	movl	-20(%rbp), %eax
	nop
.L32:
	movl	%eax, %ebx
	movl	%ebx, %eax
	addq	$136, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	_Ymain, .-_Ymain
	.ident	"GCC: (GNU) 8.0.0 20171107 (experimental)"
	.section	.note.GNU-stack,"",@progbits
