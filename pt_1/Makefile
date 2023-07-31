vuln: vuln.c
	@gcc vuln.c -o vuln -fno-stack-protector -z execstack -no-pie
	@echo "compiled!"
	@echo "run the following command to disable ASLR: sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'"

clean:
	@rm -rf vuln
	@echo "clean!"
