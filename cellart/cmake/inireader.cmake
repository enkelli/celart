#
# INIReader build.
#

add_library(inireader INTERFACE)
target_include_directories(inireader SYSTEM INTERFACE
	"${DEPS_DIR}/INIReader"
)
