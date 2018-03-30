CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(test C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fdump-tree-gimple")

FILE (
  GLOB_RECURSE
  SrcFiles
  src/*
  )

SET_SOURCE_FILES_PROPERTIES(${SrcFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(test ${SrcFiles})
target_link_libraries (test -lSDL2 -lSDL2main)
