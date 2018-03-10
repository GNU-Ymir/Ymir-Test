CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Test C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fdump-tree-gimple")

FILE (
  GLOB_RECURSE
  SourceFiles
  src/*
  )

SET_SOURCE_FILES_PROPERTIES(main.yr ${SourceFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(../test main.yr ${SourceFiles})
target_link_libraries (../test -lSDL2 -lSDL2main -lSDL2_image)
include_directories (test ./)
