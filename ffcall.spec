%define major 0
%define libavcall %mklibname avcall %{major}
%define libcallback %mklibname callback %{major}
%define devname %mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		ffcall
Version:	1.10
Release:	12
License:	GPLv2+
Group:		System/Libraries
Url:		ftp://ftp.santafe.edu/pub/gnu/
Source:		ftp://ftp.santafe.edu/pub/gnu/%{name}-%{version}.tar.bz2
Patch0:		ffcall-make-jN.patch

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
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--enable-shared
%make

%install
# make install does not create all necessary directories
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}
%makeinstall_std

mkdir -p %{buildroot}%{_defaultdocdir}/%{devname}
mv %{buildroot}%{_datadir}/html %{buildroot}%{_defaultdocdir}/%{devname}/html

chmod 0755 %{buildroot}%{_libdir}/*.so.*

