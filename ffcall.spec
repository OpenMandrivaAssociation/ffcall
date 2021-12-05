%define major 0
%define libavcall	%mklibname avcall %{major}
%define libcallback	%mklibname callback %{major}
%define devname		%mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		ffcall
Version:	2.4
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnu.org/software/lib%{name}
Source:		https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch0:		ffcall-make-jN.patch
# Upstream is dead, so this patch will not be sent. Update some uses of OABI
# on ARM to their EABI equivalents.
#Patch1:	 %{name}-arm.patch

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:
- avcall - calling C functions with variable arguments
- vacall - C functions accepting variable argument prototypes
- trampoline - closures as first-class C functions
- callback - closures with variable arguments as first-class C functions
  (a reentrant combination of vacall and trampoline)
This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

#----------------------------------------------------------------------------

%package -n %{libavcall}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11

%description -n %{libavcall}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:
- avcall - calling C functions with variable arguments
- vacall - C functions accepting variable argument prototypes
- trampoline - closures as first-class C functions
- callback - closures with variable arguments as first-class C functions
  (a reentrant combination of vacall and trampoline)
This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

%files -n %{libavcall}
%{_libdir}/libavcall.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcallback}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11
Obsoletes:	%{_lib}ffcall0 < 1.10-11

%description -n %{libcallback}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:
- avcall - calling C functions with variable arguments
- vacall - C functions accepting variable argument prototypes
- trampoline - closures as first-class C functions
- callback - closures with variable arguments as first-class C functions
  (a reentrant combination of vacall and trampoline)
This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

%files -n %{libcallback}
%{_libdir}/libcallback.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for ffcall library
Group:		Development/C
Requires:	%{libavcall} = %{EVRD}
Requires:	%{libcallback} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for ffcall library.

%files -n %{devname}
%doc NEWS README PLATFORMS
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n lib%{name}-%{version}

%build
%ifarch %arm
export CC=gcc
export CXX=g++
%endif

#export CFLAGS="%{optflags} -fPIC"
%configure
%make_build

%install
# make install does not create all necessary directories
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}
%make_install

# fix permissions
chmod 0755 %{buildroot}%{_libdir}/*.so.*

mkdir -p %{buildroot}%{_defaultdocdir}/%{devname}
mv %{buildroot}%{_datadir}/html %{buildroot}%{_defaultdocdir}/%{devname}/html

