%undefine _debugsource_packages
Name:           fast_float
Version:        8.0.2
Release:        1
Summary:        A fast number parsing library
License:        Apache-2.0 OR BSL-1.0 OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/fastfloat/fast_float
Source:         https://github.com/fastfloat/fast_float/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(doctest)

%description
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types as well as integer types.

%package devel
BuildArch:      noarch
Summary:        Development and header files for %{name}

%description devel
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types as well as integer types.

%prep
%autosetup -p1

%build
%cmake \
  -DFASTFLOAT_TEST:BOOL=ON \
  -DFASTFLOAT_SUPPLEMENTAL_TESTS:BOOL=OFF \
  -DSYSTEM_DOCTEST:BOOL=ON

%make_build

%install
%make_install -C build

%files devel
%license LICENSE-APACHE LICENSE-BOOST LICENSE-MIT
%doc README.md
%{_includedir}/fast_float
%dir %{_datadir}/cmake
%{_datadir}/cmake/FastFloat
