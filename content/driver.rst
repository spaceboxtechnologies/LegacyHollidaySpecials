======
Driver
======
A driver (or device driver) is a modular piece of software that is run by an
operating system to talk to a particular device connected to a computer.

A computer in its purest form is a CPU connected to a RAM. This is not very
useful. For example, where will your CPU get its instructions from without a
storage device? You might
opt for a ROM with instructions preinstalled but, that leaves you with a single
set of instructions to run every time (boring). Even if you've had all of these
sorted out, how will you know what your computer is doing at a point in time or how can you debug your programs without a display screen?

So, these are some of the reasons why most PC's provide many ports (internal or
external) for connecting with the CPU. For instance, you can connect your
smartphone to your computer via USB, your hard disk has a port on the
motherboard for communicating with the CPU, same applies to your display screen, mouse, even your battery, etc. 

In the middle of all these communication with the processor lies a driver. Yes,
your CPU can communicate with a connected device but it does not know how to go
about. Just like any typical software, the can solve the problem the software is
meant to solve but does not know how to go about it; that's where the software
comes. However unlike a typical software that contains mostly instructions for
the CPU to execute, a driver software typically contains instructions for the
CPU and those for the CPU to send to other connected 'computing devices' to
execute.

In the last sentence, we used the phrase 'computing devices'. Yes, that is
because most devices that connect to a computer have their own CPU. The CPU on
a typical computer (or the main processor) is usually called a general-purpose
processor, because it can perform a set of base operations that we have come to
expect from a computer, like adding, subtracting, reading from a RAM, writing to
a RAM etc. Modern computer accessories have their own 'special purpose' processor (coprocessor or microcontroller) that, maybe in addition to general CPU operations, perform other device-specific operations. Like reading a block of data from  a disk storage.

Imagine general-purpose CPU that has an instruction to read directly from a disk
storage? Although that looks cool but, it does not allow for much flexibility
and efficiency for manufacturers of disk storages. For example, some disk
storage have something called "disk scheduling" which is a feature that allows
for efficiently reading blocks of data scattered over a platter (those round
material that spin like a CD). The platter of a typical hard disk is divided and
numbered into block. So, to read let's say block 1 from the disk, there has to
be a wait for block 1 to spin before reading its data. How about reading block
1, 2 and 3? Normally, regardless of what block is already spinning, there has to
be a wait for block 1, then block 2, then block 3, in that order. So if block 3
is already spinning at the time of the read, we skip its data until its next spin
(after 1 and 2). So inefficient!!!

Back to "disk scheduling", this feature typically resides in a disk's own
processor. For our last scenario, depending on the scheduling scheme (we use
closest-first), since block 3 is already spinning, we read block 3's data, then
1, then 2. Maybe the efficiency of this does not yet ring a bell; how about
seeking block 1, 5 and 1000 while block 1000 is already spinning? Which do you
prefer? The orderly read or the scheduled read? 

Now, back to our wish for a general purpose processor with direct access to a
disk storage, like with a RAM. Imagine the symbolic form of an instruction to
read a block 1's data is "READ 1", block 2 is "READ 2" and so on. If you write a
program to read our 3 block like:

READ 1
READ 2
READ 3

This must be read in the order specified in the program regardless of the
current state of the disk platter; whether it was in block 2 or 3, at the time,
it has to go all the way to 1, then 2,then 3. No scheduling whatsoever.

We might still be stubborn and say build the scheduling feature into the memory
but that will only make building the processor unnecessarily buggy, complex and
distract a general purpose processor from its core task. Remember, this not
software. A bug at the hardware level usually requires a soldering iron, plus
bugs at this level are catastrophic and hard to find.

This one reason why many devices come with their processing units and drivers are
like the gateway to this devices as they the right set of instructions to send
to these devices' processors to make the device do something like reading a disk
block, printing on printer, displaying to a screen and so on. 

So if i say "console.log('Hello, World')" in JavaScript, my operating system identifies the
device connected to the console and checks if it has a driver for that device,
loads the driver (if not loaded already), calls the right function (somehow giving it the
location where my 'Hello, World' is stored in RAM), the driver function in turn sends (through the connection like USB) the instruction the identified device's processing unit understands for printing (again giving it my string or its location in RAM), the identified processor then finishes the printing job.
