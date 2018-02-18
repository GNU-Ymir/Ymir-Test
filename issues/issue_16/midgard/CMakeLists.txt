CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(Socket C)
SET(CMAKE_C_COMPILER "gyc")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")

FILE (
  GLOB_RECURSE
  SRC_CORE
  core/*.yr
  )

FILE (
  GLOB_RECURSE
  SRC_STD
  std/*.yr
  )

FILE (
  GLOB_RECURSE
  SRC_CORE_C
  core/*.c
  )

FILE (
  GLOB_RECURSE
  SRC_STD_C
  std/*.c
  )

SET_SOURCE_FILES_PROPERTIES(${SRC_CORE} ${SRC_STD} PROPERTIES LANGUAGE C)

add_library (gymidgard ${SRC_CORE} ${SRC_STD} ${SRC_CORE_C} ${SRC_STD_C})
target_link_libraries (gymidgard -lpthread -lgc -lgyruntime)
install (TARGETS gymidgard DESTINATION /usr/lib/)
include_directories(${CMAKE_SOURCE_DIR})














