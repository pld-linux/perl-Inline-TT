#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Inline
%define		pnam	TT
Summary:	Inline::TT Perl module - inline support for Template Toolkit 2.x
Summary(pl.UTF-8):	Moduł Perla Inline::TT - osadzanie kodu Template Toolkitu 2.x
Name:		perl-Inline-TT
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02905066df2cdb5178c13d00dea3c0c3
URL:		http://search.cpan.org/dist/Inline-TT/
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Template-Toolkit >= 2.07
BuildRequires:	perl-Test-Simple >= 0.32
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::TT  - use TT BLOCK as Perl subs. Template-Toolkit is not just
a Templating Engine. It's a language. Inline::TT is a Inline plugin to
allow you to code your Perl subs in TT.

%description -l pl.UTF-8
Moduł Inline::TT - pozwalający na używanie bloków TT jako procedur
Perla. Template-Toolkit to nie tylko mechanizm obsługujący wzorce - to
język. A Inline::TT pozwala na pisanie procedur Perla w języku TT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/TT.pm
%{_mandir}/man3/*
