#include <iostream>
#include <string>

// Classe Ville avec les attributs nom, code_postal, et pris_par_m2
class Ville {
private:
    std::string nom;      // Le nom de la ville
    int code_postal;       // La code_postal de la ville
    double pris_par_m2;    // La pris_par_m2 de la ville en km²

public:
    // Constructeur prenant directement les attributs
    Ville(std::string vill_name, int vill_code_postal, double ville_price) : nom{vill_name}, code_postal{vill_code_postal}, pris_par_m2{ville_price} {}

    // Méthode d'affichage pour afficher les détails de la ville

    void afficher() const {
        std::cout << "Ville: " << nom << std::endl;
        std::cout << "code_postal: " << code_postal << std::endl;
        std::cout << "pris_par_m2: " << pris_par_m2 << " km²" << std::endl;
    }

    // Fonction amie, surcharge de l'opérateur <<
    friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
        return out << "Nom: " << ville.nom << " | code_postal: " << ville.code_postal
                   << " | pris_par_m2: " << ville.pris_par_m2 << " Euros/km²";
    }
};

// Fonction principale qui crée une instance de Ville et l'affiche
auto main() -> int {
    // Créer une instance de Ville avec des attributs spécifiques
    Ville ville("Toulouse", 471941, 118.3);

    // Appeler la méthode afficher pour afficher les détails de la ville
    ville.afficher();

    return 0;
}