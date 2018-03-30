CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Teelol C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fdump-tree-gimple")

FILE (
  GLOB_RECURSE
  GameSourceFiles
  game/*
  common/*
  )

FILE (
  GLOB_RECURSE
  EditorSourceFiles
  editor/*
  common/*
  )

SET_SOURCE_FILES_PROPERTIES(mainGame.yr mainEditor.yr ${GameSourceFiles} ${EditorSourceFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(../teelol mainGame.yr ${GameSourceFiles})
ADD_EXECUTABLE(../teeditor mainEditor.yr ${EditorSourceFiles})
target_link_libraries (../teelol -lSDL2 -lSDL2main -lSDL2_image -lm)
target_link_libraries (../teeditor -lSDL2 -lSDL2main -lSDL2_image)
include_directories (teelol ./)
include_directories (teeditor ./)
