CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Socket C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")

FILE (
  GLOB_RECURSE
  SourceFiles
  core/*)

SET_SOURCE_FILES_PROPERTIES(client.yr server.yr ${SourceFiles} PROPERTIES LANGUAGE C)

ADD_EXECUTABLE(client client.yr ${SourceFiles})
ADD_EXECUTABLE(server server.yr ${SourceFiles})
include_directories (client ./)
include_directories (server ./)
