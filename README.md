# discrete-opt-TALight

1. Step 1: Install Rust and Cargo

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

or On Windows, download and run [rustup-init.exe](https://win.rustup.rs/). It will start the installation in a console and present the above message on success.

2. Step 2: get `typst` installed on your machine

macOS: `brew install typst`
Windows: `winget install --id Typst.Typst`

3. Step 3: clone and installa `rtal`

You should clone an `rtal` version with the capability to deal with the GIA credential, hence clone rtal from the GitHub repo:

```bash
git clone https://github.com/Guilucand/rtal-algo-client
```

```bash
cd rtal-algo-client-main
```

Changing path parameter as below here

```bash
cargo install --locked --path /Users/khoimai/rtal-algo-client-main.
```

4. Step 4: To make sure that `rtal` is correctly installed:

```bash
rtal --version
```

To see that the service for the homeworks DODM2024 is up and running:

```bash
rtal -s wss://ta.di.univr.it/DODM2024 list
```

Right now, the problems available for you to solve are:

```
- BFS
- conio1
- connected_components
- prima_PD_su_linea
```

(but we will be adding further problems during the course)

Assume you want to try out one of these problems:

```bash
rtal -s wss://ta.di.univr.it/DODM2024 get conio1
```
And the file `conio1.tar` will be downoaded in the directory you stand. Decompress this file with:

```bash
tar xvf conio1.tar
```
and you get more than the files you need to work on the problem:

```
conio1/meta.yaml  (<-- to get to know possible services available for the problem) 
conio1/example.in.txt  <-- might be helpful while debugging
conio1/testo.pdf  *** THE DESCRIPTION/EXPLANATION OF THE PROBLEM ***
conio1/example.out.txt  <-- might be helpful while debugging
conio1/README_synopsis.typ  (<-- possibly updated version)
conio1/README_rtal.typ  (<-- possibly updated version)
```
So, for every problem, the main file is `testo.pdf`, that open (and/or prints) like any other .pdf file.

*Important:* Please, if you are not confortable with Italien, and the file `testo.en.pdf` is not yet there, remind us that we have still to provide it as due.


= How to submit your solutions and get points

First thing you have to login to the service through your GIA credentials:

```bash
rtal -s wss://ta.di.univr.it/DODM2024 login
```

This will return you an URL which you open at in any browser and do the accreditation with the Verona University. This will create the needed cookies on your machine and the needed records on our server so that, from now on you can directly submit at your name from that machine.

*IMPORTANT:* if you work in group (we are very happy of that, but max 3), then it is important that:

1. all of the members of the group submit (entering at their own names)

2. in the source that you attach to the submission, possibly at the beginning (in commented lines) place the student codes (in the form VR??????) of each member of the group

3. if the source actually comprises more than one file then put the .tar of them in attachment

== Example of call
```bash
rtal -s wss://ta.di.univr.it/DODM2024 connect conio1 -f source=conio1-sol_gurobi.py -- ~/corsi/Algoritmi/esami-algo-private/esercitazioni/conio1/sol/conio1-sol_gurobi.py
```

*Note 1:* After the `--` goes whatever runs on your local machine.
For example, if you are on a Windows machine where the files ending in `.py` can not be executable files, then you would resort on writing something like:

```bash
rtal -s wss://ta.di.univr.it/DODM2024 connect conio1 -f source=conio1-sol_gurobi.py -- python ~/corsi/Algoritmi/esami-algo-private/esercitazioni/conio1/sol/conio1-sol_gurobi.py
```

*Note 2:* What your program writes on `stderr` does not disturb the interaction with the server and appears on you terminal. THerefore, `stderr` is a very useful channel for print debugging.