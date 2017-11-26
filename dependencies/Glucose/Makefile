################################################################################
# This make file serves the purpose of compiling and patching minisat for your
# platform.
#
# This file is part of the pynusmv distribution. As such it is licensed to you
# under the term of the LGPLv2. For more information regarding the legal aspect
# of this licensing, please refer to the full text of the license on the free
# software foundation website.
#
# Author: V.Feyens <victor.feyens[at] student.uclouvain.be>
################################################################################

# This target goes through all the steps required to compile MiniSat.
all: glucose.built

# This target wipes off everything that has been unpacked and built.
clean:
	rm -rf glucose
	rm glucose.unpacked
	rm glucose.patched

# This target just unpacks the zip containing minisat
glucose.unpacked:
	tar xzvf glucose-syrup-4.1.tar.gz #unzip glucose-syrup-4.1.zip
	touch glucose.unpacked

#TODO
glucose.patched: glucose.unpacked
	# Patch the makefiles to produce position independent code
	# This is necessary to create a sharedlib containing the minisat symbols
	patch -p0 -N < glucose.patch #TODO
	patch -p0 -N < glucose_simp_wrapper.patch
	patch -p0 -N < glucose_core_wrapper.patch
	touch glucose.patched

# This target proceeds to the build (proper) of the minisat codebase
glucose.built: glucose.patched
	make -C glucose
