set(SRC_DIR "${CMAKE_CURRENT_LIST_DIR}/src")
set(DEPS_DIR "${CMAKE_CURRENT_LIST_DIR}/libs")
set(INSTALL_BIN_DIR "${PROJECT_SOURCE_DIR}/bin")

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

include(ExternalProject)

include(inireader)

add_subdirectory(src)
