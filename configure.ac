#configure.ac file for python-typeutils
AC_INIT(python-typeutils, version-0.2)
#add the python m4 files
m4_include([/usr/share/aclocal-1.11/python.m4])
m4_include([/usr/share/aclocal-1.11/runlog.m4])

#check if the user specifies a specific Doxygen config file
AC_ARG_WITH(doxyfile, [  --with-doxyfile         path to doxygen config file (default: Doxyfile)])

if test "$with_doxyfile" == "yes"
then
	AC_MSG_ERROR([Please specify path to Doxyfile when using this option.])
elif test "$with_doxyfile" != ""
then
	if test -f $with_doxyfile
	then
		AC_SUBST(DOXYGEN_FILE, $with_doxyfile)
	else
		AC_MSG_ERROR([Doxygen config File $with_doxyfile not found.])
	fi
else
	if test -f Doxyfile
	then
		AC_SUBST(DOXYGEN_FILE, Doxyfile)
	else
		AC_MSG_ERROR([Python setup File $with_setup not found.])
	fi
fi

#specify the name of the setup.py file (if different from setup.py)
AC_ARG_WITH(setup, [  --with-setup            path to setup.py file (default: setup.py)])

if test "$with_setup" == "yes"
then
	AC_MSG_ERROR([Please specify path to Python setup file when using this option.])
elif test "$with_setup" != ""
then
	if test -f $with_setup
	then
		AC_SUBST(PYTHON_SETUP_FILE, $with_setup)
	else
		AC_MSG_ERROR([Python setup File $with_setup not found.])
	fi
else
	if test -f setup.py
	then
		AC_SUBST(PYTHON_SETUP_FILE,setup.py)
	else
		AC_MSG_ERROR([Python setup File $with_setup not found.])
	fi
fi

#check for python version 2.6. setup.py does this check as well
#but this will tell us where python is located. This is useful for
#the makefile
AM_PATH_PYTHON([2.6])

#check for doxygen program
AC_PATH_PROG([DOXYGEN_BINARY], [doxygen])

#specify the default prefix, for when the user does not specify it.
#this is useful as configure defaults to /usr/local while distutils
#does /usr/local.
AC_PREFIX_DEFAULT('/usr')

#output all of this into Makefile.in, producing Makefile.
AC_OUTPUT(Makefile)
