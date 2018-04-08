CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Teelol C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fdump-tree-gimple")

FILE (
  GLOB_RECURSE
  GameSourceFiles
  src/*
  )

SET_SOURCE_FILES_PROPERTIES(main.yr ${GameSourceFiles} ${EditorSourceFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(../teelol main.yr ${GameSourceFiles})
target_link_libraries (../teelol -lSDL2 -lSDL2main -lSDL2_image -lm)
include_directories (teelol ./)
