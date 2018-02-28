CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Teelol C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -lSDL2 -lSDL2main")

FILE (
  GLOB_RECURSE
  SourceFiles
  src/*
  )

SET_SOURCE_FILES_PROPERTIES(main.yr ${SourceFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(teelol main.yr ${SourceFiles})
include_directories (teelol ./)
