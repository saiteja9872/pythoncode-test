# import argparse
# import os
# import sys
# makfele_1 = """
# #
# #  This file is part of MUMPS 5.3.5, released
# #  on Thu Oct 22 09:29:08 UTC 2020
# #
# # These settings for a PC under Debian/linux with standard packages :
# # metis (parmetis), scotch (ptscotch), openmpi, gfortran
#
# # packages installation:
# # apt-get install libmetis-dev libparmetis-dev libscotch-dev libptscotch-dev libatlas-base-dev openmpi-bin libopenmpi-dev liblapack-dev
#
# # Begin orderings
# #LSCOTCHDIR = /home/amd/pradeep/spack/spack/opt/spack/linux-centos7-zen2/gcc-9.1.1/scotch-6.0.10-yemyf6c4wwhzsxys3d4krfoxsonzncbe/lib
# #ISCOTCH   = -I/home/amd/pradeep/spack/spack/opt/spack/linux-centos7-zen2/gcc-9.1.1/scotch-6.0.10-yemyf6c4wwhzsxys3d4krfoxsonzncbe/include
# LSCOTCHDIR = /home/amd/chithra/scotch_6.1.0/lib
# ISCOTCH   = -I/home/amd/chithra/scotch_6.1.0/include
#
# LSCOTCH   = -L$(LSCOTCHDIR) -lptesmumps -lptscotch -lptscotcherr -lesmumps -lscotch -lscotcherr
# #LSCOTCH   = -L$(LSCOTCHDIR) -lesmumps -lscotch -lscotcherr
#
# LPORDDIR = $(topdir)/PORD/lib/
# IPORD    = -I$(topdir)/PORD/include/
# LPORD    = -L$(LPORDDIR) -lpord
#
# LMETISDIR =
# """
#
# makfele_2 = """
# IMETIS    = -I{METIS_PATH}/include
# LMETIS    = -L{METIS_PATH}/lib -lmetis
# """
#
# makfele_3 = """
#
# # Corresponding variables reused later
# ORDERINGSF = -Dmetis
# ORDERINGSC  = $(ORDERINGSF)
#
# LORDERINGS = $(LMETIS)
# IORDERINGSF =
# IORDERINGSC = $(IMETIS)
# # End orderings
# ################################################################################
#
# PLAT    =
# LIBEXT  = .so
# OUTC    = -o
# OUTF    = -o
# RM = /bin/rm -f
# CC = mpiicc
# FC = mpiifort
# FL = mpiifort
# AR = ar vr
# RANLIB = ranlib
# """
#
# makfele_4 = """
# AOCLROOT={LIBS_PATH}
# LAPACK = -L{LIBS_PATH}/libflame_install/lib -lflame
# SCALAP = -L{LIBS_PATH}/aocl-scalapack/build/lib -lscalapack
# """
#
# makfele_5 = """
# INCPAR =   # not needed with mpif90/mpicc:  -I/usr/include/openmpi
#
# LIBPAR = $(SCALAP) $(LAPACK) -lmpi_ilp64 # not needed with mpif90/mpicc: -lmpi_mpifh -lmpi
#
# INCSEQ = -I$(topdir)/libseq
# LIBSEQ  = $(LAPACK) -L$(topdir)/libseq -lmpiseq
# """
#
# makfele_6 = """
# LIBBLAS = -L{LIBS_PATH}/blis_install/lib -lblis-mt
# LIBOTHERS = -liomp5 -lpthread
# """
#
# makfele_7 = """
#
# #Preprocessor defs for calling Fortran from C (-DAdd_ or -DAdd__ or -DUPPER)
# CDEFS   = -DAdd_
#
# #Begin Optimized options
# OPTF    = -fpp -fno-alias -O3 -fp-model precise -DMUMPS -DDDM -D_IMPLICITNONE -Dintel_ -DMPI_I8 -nofor-main -assume byterecl -qopenmp -O -fPIC -DBLR_MT -DGEMMT_AVAILABLE -DALLOW_NON_INIT -i8 #-DWORKAROUNDINTELILP64MPI2INTEGER
# OPTL    = -nofor-main -qopenmp -O -fPIC
# OPTC    = -mp1 -qopenmp -qopenmp-threadprivate=compat -fPIC -O -DGEMMT_AVAILABLE -DDETERMINISTIC_PARALLEL_GRAPH -DLRMUMPS -DBLR_MT -DINTSIZE64 -DMKL_ILP64
# #OPTF    = -nofor-main -qopenmp -O -fPIC -DBLR_MT -DGEMMT_AVAILABLE -DALLOW_NON_INIT -i8 #-DWORKAROUNDINTELILP64MPI2INTEGER
# #OPTL    = -nofor-main -qopenmp -O -fPIC
# #OPTC    = -qopenmp -O -fPIC -DINTSIZE64 -DMKL_ILP64
# #End Optimized options
#
# INCS = $(INCPAR)
# LIBS = $(LIBPAR)
# LIBSEQNEEDED =
#
# """
#
#
# class CreateMakeFile:
#     def __init__(self, **kwargs):
#         self.ARGS = kwargs
#
#         self.file_obj = open("Makefile.inc", "w")
#
#     def __call__(self, **kwargs):
#         self.ARGS = kwargs
#         self.write2file()
#         self.savefile()
#
#     def write2file(self):
#         self.file_obj.write(makfele_1)
#         self.file_obj.write(makfele_2.format(METIS_PATH=self.ARGS["METISPATH"]))
#         self.file_obj.write(makfele_3)
#         self.file_obj.write(makfele_4.format(LIBS_PATH=self.ARGS["LIBSPATH"]))
#         self.file_obj.write(makfele_5)
#         self.file_obj.write(makfele_6.format(LIBS_PATH=self.ARGS["LIBSPATH"]))
#         self.file_obj.write(makfele_7)
#
#     def savefile(self):
#         self.file_obj.close()
# #         print("Makefile.inc generataed successfully........!")
# #
# #
# # def main():
# #     parser = argparse.ArgumentParser()
# #     parser.add_argument("-M", type=str, required=True, help="METIS PATH")
# #     parser.add_argument("-L", type=str, required=True, help="LIBS PATH")
# #     args = parser.parse_args()
# #     print(args)
# #
# #     Makefilecreate_obj = CreateMakeFile()
# #     Makefilecreate_obj(METISPATH=args.M,
# #                        LIBSPATH=args.L)
# #
# #
# # if __name__ == "__main__":
# #     main()
# #
# #
#
#
# x = "they're bill's friends from the UK".title()
# print(x)
#
# import string
# x = string.capwords("they're bill's friends from the UK")
# print(x)
#
# print("they're bill's friends from the UK".capitalize())
# print("they're bill's friends from the UK".upper())
#
# y = ""
# for x in "they're bill's friends from the UK".split(" "):
#     y = y+x.capitalize()+" "
# print(y)
#
# # Python 3 code to demonstrate
# # removing duplicate elements from the list
# l = [1, 2, 4, 2, 1, 4, 5]
# print("Original List: ", l)
# res = list(set(l))
# print("List after removing duplicate elements: ", res)

# number=[1,6,5,9,0]
# for i in range(len(number)):
#   for j in range(i+1,len(number)):
#     if number[i]<number[j]:
#       number[i],number[j]=number[j],number[i]
# print(number)
#
#
# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys()))
# print(list(mydict.values()).index(19))
# print(list(mydict.keys())[list(mydict.values()).index(19)])
#
# class A:
#     def __init__(self, books):
#         self.books = books
#         self.__a = "asdasd"
#
#     def f1(self):
#         print("Hi")
#         print("{}".format(self.books))
#
#     def __f2(self):
#         print("hello")
#
# class B(A):
#     def __init__(self, numbers, books):
#         super(B, self).__init__(books)
#         self.numbers = numbers
#
#     def f1(self):
#         print("Hello")
#         print(self.numbers)
#
# class C(B, A):
#     def __init__(self, books, numbers):
#         super(C, self).__init__(books, numbers)
#
# obj = C("xyz", 20)
# obj.f1()
#
#

# import pandas as pd
# import numpy as np
# #
# # data = pd.DataFrame(np.arange(16).reshape((4,4)), index=['a1', 'b1', 'c1', 'd1'], columns=[1, 2, 3, 4])
# #
# # print(data)
# # print(data.tail(2))
# # print(data.drop(labels=['a1', 'b1'], axis=0))
# #
# #
# # # Delete a single named column from the DataFrame
# # data = data.drop(columns=2)
# # print(data)
# # # Delete multiple named columns from the DataFrame
# # # data = data.drop(columns=["cases", "cases_per_million"])
#
#
#
#
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj1 = pd.Series(sdata, index=states)
#
# print(obj1)




#
# #
# # # Python program to
# # # demonstrate private members
# #
# # # Creating a Base class
# #
# #
# class Base:
#     def __init__(self):
#         self.a = "Sample"
#         self.__c = "Hello"
#
#     def __myprint(self):
#         print("myprint")
#
#     def samplerun(self):
#         print("hh")
#
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         # Base.__init__(self)
#         print("Calling private member of base class: ")
#         # print(self._Base__c)
#
#     def samplerun(self):
#         super().samplerun()
#         print("oo")
#
#
# # Driver code
# obj1 = Base()
# # print(dir(obj1))
# # print(obj1.a)
# # # print(obj1.c)
# # print(obj1._Base__c)
# # Uncommenting obj2 = Derived() will
# obj2 = Derived()
# print(dir(obj2))
# print(obj2.a)
# print(obj2._Base__c)
#
# obj2._Base__myprint()
#
# obj2.samplerun()
# obj1.samplerun()

# l = [2, 3, 1, 4, 5]
#
#
# def min(x):
#     min1 = max = l[0]
#     min2 = l[0]
#     for i in l[1:]:
#         if i < min1:
#             min1 = i
#         else:
#             if min2 > i:
#                 min2 = i
#             max = i
#     return min1, min2, max
#
# print(min(l))

#
#
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] < l[j]:
#             l[i], l[j] = l[j], l[i]
#
# print(l[-2])


#
# t=(1, 2)
# # [ for i, v in enumerate(l) ]
#
#
# t=(1,3)
#
#
# x1 = []
#
# x2 = copy.copy()


# def mydec(fun):
#     def wrapper(x):
#         print(x)
#         fun()
#         print(x)
#     return wrapper
#
# @mydec
# def fun(x):
#     pass
#
#
#
#
#
# class A:
#     def __init__(self):
#         self.a = 1
#         self.__c = 2
#
#     def __myfn(self):
#         print("hi")
#
# obj  = A()
# print(dir(obj))
#
#
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @classmethod
#     def f1(cls):
#         pass


# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://127.0.0.1/dbanalysist")
# print(myclient)
# mydb = myclient["mydatabase1"]
# print(mydb)
# # print(myclient.list_database_names())


# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# print(mycol)
# print(mydb.list_collection_names())

import numpy as np
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[0])

























