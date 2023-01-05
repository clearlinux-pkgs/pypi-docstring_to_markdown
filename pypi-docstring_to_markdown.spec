#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-docstring_to_markdown
Version  : 0.11
Release  : 4
URL      : https://files.pythonhosted.org/packages/e9/68/cac92c4f3f837fbeba17e8dfcdb7658fac6a1d56c007ed0d407087f1127e/docstring-to-markdown-0.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/e9/68/cac92c4f3f837fbeba17e8dfcdb7658fac6a1d56c007ed0d407087f1127e/docstring-to-markdown-0.11.tar.gz
Summary  : On the fly conversion of Python docstrings to markdown
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: pypi-docstring_to_markdown-license = %{version}-%{release}
Requires: pypi-docstring_to_markdown-python = %{version}-%{release}
Requires: pypi-docstring_to_markdown-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# docstring-to-markdown
[![tests](https://github.com/python-lsp/docstring-to-markdown/workflows/tests/badge.svg)](https://github.com/python-lsp/docstring-to-markdown/actions?query=workflow%3A%22tests%22)
![CodeQL](https://github.com/python-lsp/docstring-to-markdown/workflows/CodeQL/badge.svg)
[![pypi-version](https://img.shields.io/pypi/v/docstring-to-markdown.svg)](https://python.org/pypi/docstring-to-markdown)

%package license
Summary: license components for the pypi-docstring_to_markdown package.
Group: Default

%description license
license components for the pypi-docstring_to_markdown package.


%package python
Summary: python components for the pypi-docstring_to_markdown package.
Group: Default
Requires: pypi-docstring_to_markdown-python3 = %{version}-%{release}

%description python
python components for the pypi-docstring_to_markdown package.


%package python3
Summary: python3 components for the pypi-docstring_to_markdown package.
Group: Default
Requires: python3-core
Provides: pypi(docstring_to_markdown)

%description python3
python3 components for the pypi-docstring_to_markdown package.


%prep
%setup -q -n docstring-to-markdown-0.11
cd %{_builddir}/docstring-to-markdown-0.11
pushd ..
cp -a docstring-to-markdown-0.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672269481
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-docstring_to_markdown
cp %{_builddir}/docstring-to-markdown-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-docstring_to_markdown/b386b371ce94933e63ced1052aa72a60da5485ff || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-docstring_to_markdown/b386b371ce94933e63ced1052aa72a60da5485ff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
