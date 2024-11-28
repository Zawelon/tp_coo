#include <iostream>
#include <string>

// Classe Ville avec les attributs nom, code_postal, et prix_par_m2
class Ville {
  std::string nom;    // Le nom de la ville
  int code_postal;    // Le code postal de la ville
  float prix_par_m2;  // Le prix par mètre carré dans la ville

 public:
  // Constructeur utilisant une liste d'initialisation
  Ville(std::string n, int code, float prix)
      : nom{n}, code_postal{code}, prix_par_m2{prix} {}

  // Fonction amie, surcharge de l'opérateur <<
  friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
    return out << "Nom: " << ville.nom
               << " | Code postal: " << ville.code_postal
               << " | Prix par m²: " << ville.prix_par_m2 << " €";
  }
};

int main() {
  // Créer un objet Ville
  Ville ville("Toulouse", 31000, 3500.5);

  // Utiliser l'opérateur << surchargé pour afficher les informations de l'objet
  std::cout << ville << std::endl;

  return 0;
}
