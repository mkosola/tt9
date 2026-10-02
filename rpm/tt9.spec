Name:       tt9
Summary:    Keypad layouts and predictive dictionaries for Sailfish OS
Version:    1.0
Release:    1
License:    Apache-2.0 and MIT and BSD-3-Clause and GPL-2.0-or-later and GPL-3.0-only and LGPL-2.1-or-later and LGPL-3.0-only and AGPL-3.0-only and MPL-2.0 and CC0-1.0 and CC-BY-3.0 and CC-BY-4.0 and CC-BY-SA-4.0 and ODbL-1.0 and LicenseRef-Database-Contents and LicenseRef-GFDL-Unverified and LicenseRef-Public-Domain and LicenseRef-Unresolved
BuildArch:  noarch
URL:        https://github.com/sailfishos/tt9
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: python3-base
BuildRequires: python3-sqlite

%description
Keypad layouts from Traditional T9, one locale layout file per language, plus
word lists for the locales named in dictionaries.list. The Sailfish OS keypad
reads both from %{_datadir}/keypad. A layout is enough for the letters.
Prediction needs the matching sqlite file.


%package layouts
Summary:    Keypad layouts from Traditional T9
License:    Apache-2.0

%description layouts
Keypad layouts from Traditional T9 for Sailfish OS.


%package dictionary-de-de
Summary:    Keypad dictionary for de-DE from Traditional T9
License:    GPL-2.0-or-later
Requires:   %{name}-layouts

%description dictionary-de-de
Word list for de-DE from Traditional T9, for keypad prediction.


%package dictionary-en
Summary:    Keypad dictionary for en from Traditional T9
License:    GPL
Requires:   %{name}-layouts

%description dictionary-en
Word list for en from Traditional T9, for keypad prediction.


%package dictionary-fi-fi
Summary:    Keypad dictionary for fi-FI from Traditional T9
License:    GPL-3.0-only
Requires:   %{name}-layouts 

%description dictionary-fi-fi
Word list for fi-FI from Traditional T9, for keypad prediction.


%prep
%autosetup -n %{name}-%{version}

%build
python3 build-dictionaries.py --output tt9-data --notices tt9-notices \
    --from-list languages.list --dictionaries dictionaries.list

%install
mkdir -p %{buildroot}%{_datadir}/keypad
cp -a tt9-data/. %{buildroot}%{_datadir}/keypad/

%files layouts
%license tt9/LICENSE.txt
%dir %{_datadir}/keypad
%{_datadir}/keypad/*.layout

%files dictionary-de-de
%%license tt9-notices/de-DE.txt tt9-notices/de-DE.license
%{_datadir}/keypad/de-DE.sqlite

%files dictionary-en
%%license tt9-notices/en.txt tt9-notices/en.license
%{_datadir}/keypad/en.sqlite

%files dictionary-fi-fi
%%license tt9-notices/fi-FI.txt tt9-notices/fi-FI.license
%{_datadir}/keypad/fi-FI.sqlite
