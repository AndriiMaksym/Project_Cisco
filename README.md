Główny skrypt wykorzystuje język Python do gromadzenia, analizowania i ewentualnie wizualizacji danych dotyczących zdrowia, pomagając użytkownikom monitorować ich wskaźniki zdrowotne na przestrzeni czasu.
JavaScript jest używany wyłącznie do diagramów w projekcie, korzystał z biblioteki chart.js

==================================================================================================================================================
Składniki funkcjonalne:
Autoryzacja użytkowników:
  Logowanie: Umożliwia użytkownikom logowanie się na swoje konta.
  Wylogowanie: Umożliwia użytkownikom wylogowanie się ze swoich kont.
  Rejestracja: Umożliwia nowym użytkownikom tworzenie kont.
==================================================================================================================================================
Zarządzanie danymi zdrowotnymi:
  Użytkownicy mogą rejestrować swoje posiłki, w tym szczegóły takie jak typ posiłku, kalorie, białka i tłuszcze.

  Aktywności: Użytkownicy mogą rejestrować swoje aktywności fizyczne, w tym szczegóły takie jak typ aktywności, czas trwania i spalone kalorie.

  Wpisy wagowe: Użytkownicy mogą rejestrować swoje wpisy wagowe z datą i wagą.
=================================================================================================================================================
Analiza danych i wizualizacja:

Strona przeglądu: Wyświetla średnie statystyki dotyczące kalorii, białek, tłuszczy, czasu trwania aktywności, spalonych kalorii i wagi.
Wykresy: Wizualizuje dane zdrowotne za pomocą Chart.js, aby dostarczyć wglądu w aktywności użytkownika i spożycie kalorii.

Rozróżnienie administratora i użytkownika:
  Widok administratora: Administratorzy mają dodatkowe uprawnienia lub widoki, co jest sygnalizowane przez obecność specjalnych znaczników lub wiadomości w     
interfejsie.
  Widok użytkownika: Zwykli użytkownicy mają dostęp do swoich zarejestrowanych danych i mogą zobaczyć spersonalizowane statystyki.