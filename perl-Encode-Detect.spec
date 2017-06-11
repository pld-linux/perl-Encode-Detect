#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Encode
%define	pnam	Detect
Summary:	Encode::Detect - An Encode::Encoding subclass that detects the encoding of data
Summary(pl.UTF-8):	Encode::Detect - podklasa Encode::Encoding wykrywająca kodowanie danych
Name:		perl-Encode-Detect
Version:	1.01
Release:	11
License:	MPL 1.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee9faf55d7105c97b02b8ebe590819c7
URL:		http://search.cpan.org/dist/Encode-Detect/
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build >= 0.2808
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-Dump
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data
and then decodes it using the encoder of the detected charset.

It is similar to Encode::Guess, but does not require the configuration
of a set of expected encodings. Like Encode::Guess, it only supports
decoding - it cannot encode.

%description -l pl.UTF-8
Ten moduł Perla jest podklasą Encode::Encoding wykorzystującą
Encode::Detect::Detector do określenia zestawu znaków danych
wejściowych i dekodującą je przy użyciu kodera dla wykrytego zestawu
znaków.

Moduł ten jest podobny do Encode::Guess, ale nie wymaga konfiguracji
zbioru oczekiwanych kodowań. Podobnie jak Encode::Guess obsługuje
tylko dekodowanie; nie potrafi kodować.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--extra-compiler-flags='%{rpmcflags} -x c++ -Iinclude' \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Encode/*.pm
%{perl_vendorarch}/Encode/Detect
%dir %{perl_vendorarch}/auto/Encode/Detect
%dir %{perl_vendorarch}/auto/Encode/Detect/Detector
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Detect/Detector/*.so
%{_mandir}/man3/*
