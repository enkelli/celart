set(CELLART_SOURCES
	ca.cpp
	main.cpp
	rules.cpp
)

add_executable(cellart ${CELLART_SOURCES})
target_include_directories(cellart PUBLIC "${SRC_DIR}")
target_link_libraries(cellart PUBLIC
	inireader
)
install(TARGETS cellart DESTINATION "${INSTALL_BIN_DIR}")
