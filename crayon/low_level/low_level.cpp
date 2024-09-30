#include "iostream"

class Departement() {
  std::string nom;
  int code_postal;
  float pris_par_m2;

  // Constructeur  sans parametre
  Departement() {
    nom = "Non defini";
    code_postal = 0;
    pris_par_m2 = 0;
  }

  // Constructeur  avec parametres
  Departement(std::string nom, int code_postal, int pris_par_m2) {
    this->nom = nom;
    this->code_postal = code_postal;
    this->pris_par_m2 = pris_par_m2;
  }

  // Methode d'affichage
  void Affichage() {
    std::cout << "Le nom du departement est: " << nom << std::endl;
    std::cout << "Le code postal est: " << code_postal << std::endl;
    std::cout << "Le le prix par metre carre est: " << pris_par_m2 << std::endl;
  }
}
