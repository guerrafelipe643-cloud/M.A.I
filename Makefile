# Configurações
CXX = g++

CXXFLAGS = -std=c++17 -Wall -Wextra -O3
TARGET = listlink
SRCDIR = src
BUILDDIR = build

# Arquivos
SOURCES = $(wildcard $(SRCDIR)/*.cpp)

OBJECTS = \
$(patsubst \
$(SRCDIR)/%.cpp,\
$(BUILDDIR)/%.o,\
$(SOURCES))

all: $(TARGET)

# LINKAGEM
$(TARGET): $(OBJECTS)
	@mkdir -p $(BUILDDIR)
	$(CXX) \
	$(CXXFLAGS) \
	$^ \
	-o $@ \

# COMPILAÇÃO
$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(BUILDDIR)

	$(CXX) \
	$(CXXFLAGS) \
	-c $< \
	-o $@

clean:
	rm -rf \
	$(BUILDDIR) \
	$(TARGET)

.PHONY: all clean