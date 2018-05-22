Summary:	GNU Gengen - parameterized-text-generator generator based on a template
Summary(pl.UTF-8):	GNU Gengen - generator generatorów sparametryzowanego tekstu w oparciu o wzorzec
Name:		gengen
Version:	1.4.2
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/gengen/%{name}-%{version}.tar.gz
# Source0-md5:	4559df90480d304e127841eb22a54985
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/gengen/
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Gengen (GENerator GENerator) is a tool that, starting from a
parameterized text, called template, generates a text generator that
can substitute parameters with values.

%description -l pl.UTF-8
GNU Gengen (GENerator GENeratorów) to narzędzie potrafiące ze
sparametryzowanego tekstu (nazywanego wzorcem) wygenerować generator
tekstu podstawiający wartości zamiast parametrów.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gengen

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS doc/{gengen,index}.html
%attr(755,root,root) %{_bindir}/gengen
%{_mandir}/man1/gengen.1*
%{_infodir}/gengen.info*
