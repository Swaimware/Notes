# Linux

## Versions

* Pop OS
* Ubuntu
* Mint

## Software Package Manager

* Use launchpad to create .deb packages - Advanced

## Tools

* Use balena etcher to make USB installs
* Had to setup SSH with Gitlab
* sudo apt install tmux
* Installed Alacritty
* Installed tmatrix
* sudo apt install vim
* sudo apt install git
* sudo apt install htop
* sudo apt install curl 
* sudo apt install xclip

## Command Line

### Character

* ' >   redirect output   example  ls -l > output.txt
* ' > output.txt   creates empty txt file
* ' >>  redirect that appends the file as opposed to overwriting it
* 2>  redirect error  0 = Standard Input 1 = Standard Output 2 = Standard error
* &>  redirects both output and error
* ls -l /bin/usr 2> /dev/null   sends error to bit bucket - throws away
* <   reverse the redirection
* command1 | command2   output of command1 is piped | into the input of command2
* ls /bin /usr/bin | sort | uniq | less    chaining pipes

### A

* alias name='string'   can create command like 'mkdir dir; cd dir;'  unalias name removes it
* apropos word   searches the man pages for the word

### C

* cal   displays current month calender
* cat  spits out contents out of a file
* cd Di  then press tab auto-completes
* cd .. back one directory
* cd    by itself with go to home  or cd ~
* cd -  takes you back to the last directory
* cd /  takes you the root
* cd tab twice shows all directory in path
* chmod +x bashfilename   makes file executable
* because the file is not in PATH execute with  ./bashfilename
* clear clears screen
* cp ~/.vimrc .   this command copies .vimrc on home directory to current directory
* cp options: -a --archive used to copy permissions with -i gives warning if file/dir exists
* -r --recursive   -u --update copies if newer or doesnt exist -v --verbose
* CTRL C  will intterupt running program
* CTRL D  end of file
* CTRL S  suspends terminal  dont do

### D

* date  displays current date and time
* df     displays free space on drives
* diff file1 file2  shows difference

### E

* echo $PATH   to show directories in the path
* exec bash   replaces current shell with a new one with install

### F

* free   displays available memory
* file filename  displays what type of file it is

### G

* grep pattern file   finds the pattern in the file, pattern could be a regex
* example: ls /bin /usr/bin | sort | uniq | grep zip   displays all file names with zip in it

### H
* head -n 5 file.txt    prints first 5 lines  the -f creates a real time view
* tail -n 5 file.txt    prints last 5 lines
* help builtin-command  gives instructions  also  command --help  works

### I

* info coreutils   information on GNU programs

### L

* less filename  view text files
* ln  creates a symbolic link
* ls -a   lists all including hidden  -A almost all excludent current/parent director
* ls -d Repos/   shows the directory path?
* ls -F  classify   shows / after dir
* ln -s $PWD/bashconfig $HOME/.bash_aliases    symbolically link files
* ls -l $HOME/.bash_aliases   shows the linking
* ls -l    gives detail listing of directory
* ls -ld   gives details about dir
* ls -ld ~/usr   specify which dir
* ls -r  reverse sort  -s sort by size  -t  sort by date/time  
* ls --help    or   man ls  for help but internet is better for beginner

### M
* man command  displays instructions for command, more descriptive than help
* MKDIR   make directory, can make multiple at one time
* mv   moves
* mv options: -i --interactive  -u --update  -v --verbose
* mv .vimrc vimrc   renames file

### P

* ping gitlab.com
* PWD or $PWD

### R

* rm filename    removes filename or a directory
* rm options -i --interactive  -r --recursive  -f --force  -v --verbose

### S

* set -o vi   turns your search history into a VI file that you can see one line at a time, can do all VI commands
* sudo su - sample   logs you in as a new user (sample)

### T

* tee   creates a tee in the pipline allowing input to be stored to file.txt and sent to next pipline as output
* top    shows all running processes
* if you create alias for top  then \top will disable alias
* touch   updates timestamp on file (but also creates new one)
* type command   shows what type is the command.  Possible types: executable, builtin. shell function,or an alias

### V

* vi filename   opens filename in vi
* view filename  uses vi to read safely, much like the less command

### w

* wc file.txt  gives number of lines, words, bytes  can use -l to just give lines
* Wild Cards
* *  match any number of characector
* ?  match any one characector
* [characters]  matches set of characters
* [!characters] does not match set of characters
* [:class:]   [:alnum:] match any alphanumeric characters
*             [:alpha:] match any alphapetic characters
*             [:digit:]  [:lower:]  [:upper:]
* whatis command   gives a one-line description of command
* which executable-command  show location of exe-command

### X

* xclip  copies contents of a file into clipboard

## BASH

* When a terminal starts the .bashrc and .profile (for logins) are ran
* chmod +x bashfilename   compiles the bash text file into an executable
* ix < ix    ix is a script that sets up a short URL, in this case sending the script ix
* curl http://ix.io/2iTo will spit out contents on shell, in this case the ix script
* curl http://ix.io/2iTO > ix   will redirect to file called ix


## VIM RESOURCES

* vimtutor
* openvim.com
* vimgenius.com
* yannesposito.com/scratch/en/blog/learn-vim-progressively/
* the magic wands
* curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

## VIM

* i     puts VI into insert mode - place text before cursor
* a     append mode - place text after cursor
* ESC   takes you back out of insert mode
* :     goes into command mode
* :q!   quits without making any changes - must be in normal mode
* :wq    quits saving changes - must be in normal mode
* ZZ    same as above just easier
* x     deletes characector while in normal mode
* dw    move cursor at beginnig of word ad use dw to delete word in normal mode
* de    deletes word starting from end of word
* d$    deletes to end of line in normal mode
* w, e, $  moves cursor without deletion
* d3w   deletes 3 words
* 0     goes to begining of line

* vimtutor  self explanitory
 

## SSH keys

* ssh-keygen -t ed25519
* press return twice to accept default dir and no passcoded
* cd
* xclip < ~/.ssh/id_ed25519.pub
* now paste into gitlab.com
* SSH git@gitlab.com  verifies SSH key done correctly

## git from existing directory

* git gittutorial   learn git

* git init
* git remote add origin git@gitlab.com:swaimware/eightball.git
* git remote add origin https://github.com/Swaimware/test.git
* git add .
* git status
* git commit -m "initial commit"
* git branch -M main
* git status
* git push -u origin main
* git pull
* which git   shows location
* git --version
* git remote rm origin       removes the origin




