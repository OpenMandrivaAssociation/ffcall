%define	name	ffcall
%define libname_orig    lib%{name}
%define	version	1.10
%define	release	%mkrel 4

%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Development/C
URL:		ftp://ftp.santafe.edu/pub/gnu/
Source:		ftp://ftp.santafe.edu/pub/gnu/%{name}-%{version}.tar.bz2
Buildrequires:	autoconf2.5

%package 	-n %{libname}
Summary:        Libraries that can be used to build foreign function call interfaces
Group:          Development/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}
Provides:	%{libname_orig} = %{version}-%{release}
Conflicts:      %mklibname %{name} 0 -d

%package        -n %{libnamedev}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:          Development/Other
Provides:	%{libname_orig}-devel 
Provides:	%{name}-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}
Obsoletes:	%mklibname %{name} 0 -d

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
    (a reentrant combination of vacall and trampoline)

    This version B includes some minor configuration changes so that files
    are installed in the proper place. Also it compiles on cygwin and mingw32.

%description -n %{libname}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
    (a reentrant combination of vacall and trampoline)

    This version B includes some minor configuration changes so that files
    are installed in the proper place. Also it compiles on cygwin and mingw32.


%description -n %{libnamedev}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --enable-shared
make

%install
rm -rf ${buildroot}
# make install does not create all necessary directories
mkdir -p %buildroot %buildroot/%_includedir %buildroot/%_libdir %buildroot/%_mandir
%makeinstall_std

mkdir -p %{buildroot}%{_defaultdocdir}/%{libnamedev}
mv %{buildroot}/usr/share/html %{buildroot}%{_defaultdocdir}/%{libnamedev}/html

%clean
rm -rf ${buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc NEWS README PLATFORMS
%_includedir/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
