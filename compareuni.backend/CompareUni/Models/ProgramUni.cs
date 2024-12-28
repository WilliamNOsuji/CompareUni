using Microsoft.EntityFrameworkCore.Metadata;
using System.ComponentModel;

namespace CompareUni.Models
{
    public class UniProgram
    {
        public UniProgram()
        {

        }
        [DisplayName("Program Nom")]
        public string Nom { get; set; }

        [DisplayName("Nombre de crédits et durée")]
        public string Credits { get; set; }

        [DisplayName("Session d'admission et dates limites")]
        public string Admission { get; set; }

        [DisplayName("Cycle")]
        public string Cycle { get; set; }

        [DisplayName("Contingentement")]
        public string Contingent { get; set; }

        [DisplayName("Régime des études")]
        public string Regime { get; set; }
        [DisplayName("Langue d'enseignement")]
        public string Langue { get; set; }
        [DisplayName("Stages")]
        public string Stage { get; set; }
        [DisplayName("Grade")]
        public string Grade { get; set; }
        [DisplayName("Description et Détails du programme")]
        public string Description { get; set; }
        [DisplayName("Conditions D'Admission")]
        public string ConditionsAdmission { get; set; }

    }
}
