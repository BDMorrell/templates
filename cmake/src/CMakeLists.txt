file(GLOB SOURCES_MAIN ./*.cpp)
file(GLOB HEADERS_MAIN ./*.h)

add_executable(>>EXECNAME<< ${SOURCES_MAIN} ${HEADERS_MAIN})

