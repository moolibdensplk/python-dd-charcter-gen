from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from internal.dice import *
import jinja2
import pdfkit
import platform


class DDMainMenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DDMainMenuWindow, self).__init__()
        loadUi("ui/mainWindow.ui", self)
        self.character_class = self.classSelectionBox.currentText()
        self.strength = get_character_stat(roll4xd6())
        self.dexterity = get_character_stat(roll4xd6())
        self.constitution = get_character_stat(roll4xd6())
        self.inteligence = get_character_stat(roll4xd6())
        self.wisdom = get_character_stat(roll4xd6())
        self.charisma = get_character_stat(roll4xd6())
        self.character_race = ""
        self.character_name = ""



        # class dorpdown - on update/select generate hit points
        self.classSelectionBox.activated.connect(self.update_sheet)
        self.raceSelectionBox.activated.connect(self.set_character_race)

        # initial character stats in the table
        self.statsTable.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.strength)))
        self.statsTable.setItem(1, 0, QtWidgets.QTableWidgetItem(str(self.dexterity)))
        self.statsTable.setItem(2, 0, QtWidgets.QTableWidgetItem(str(self.constitution)))
        self.statsTable.setItem(3, 0, QtWidgets.QTableWidgetItem(str(self.inteligence)))
        self.statsTable.setItem(4, 0, QtWidgets.QTableWidgetItem(str(self.wisdom)))
        self.statsTable.setItem(5, 0, QtWidgets.QTableWidgetItem(str(self.charisma)))
        self.statsTable.setItem(0, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.strength))))
        self.statsTable.setItem(1, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.dexterity))))
        self.statsTable.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.constitution))))
        self.statsTable.setItem(3, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.inteligence))))
        self.statsTable.setItem(4, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.wisdom))))
        self.statsTable.setItem(5, 1, QtWidgets.QTableWidgetItem(str(self.get_stat_mod(self.charisma))))

        # set the saving throw table values
        #self.savingThrowTable.setItem()
        self.save_modifiers = self.get_char_save_modifiers(self.character_class)
        self.savingThrowTable.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Strength"])))
        self.savingThrowTable.setItem(1, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Dexterity"])))
        self.savingThrowTable.setItem(2, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Constitution"])))
        self.savingThrowTable.setItem(3, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Intelligence"])))
        self.savingThrowTable.setItem(4, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Wisdom"])))
        self.savingThrowTable.setItem(5, 0, QtWidgets.QTableWidgetItem(str(self.save_modifiers["Charisma"])))

        # connecting buttons
        self.statsRollButton.clicked.connect(self.reroll_stats)
        constitution_modifier = self.statsTable.item(2,1).text()
        # print("DEBUG: INITIAL CON MOD: %s " % constitution_modifier)
        # print("DEBUG: INITIAL character class: %s" % self.character_class)
        self.initialHP = self.generate_hit_points(self.character_class, constitution_modifier)
        # print("DEBUG: INITIAL HP: %s" % str(self.initialHP))
        self.hpReRoll.clicked.connect(self.reroll_hp)

        # character name:
        self.characterNameEdit.setMaxLength(32)
        self.characterNameEdit.textChanged.connect(self.set_character_name)

        # update labels
        self.hitPointsLabel.setText(str(self.initialHP))

        # generate pdf button
        self.genCharSheet.clicked.connect(self.gerate_pdf_sheet)

# button and menu functions
    def generate_hit_points(self, character_class, con_mod):

        hp_roll = 1
        max_hit_points = hp_roll + int(con_mod)
        if self.character_class == "Wizard":
            hp_roll = rolld4()
            max_hit_points = hp_roll + int(con_mod)
        elif self.character_class == "Rogue":
            hp_roll = rolld6()
            max_hit_points = hp_roll + int(con_mod)
        elif self.character_class == "Cleric":
            hp_roll = rolld8()
            max_hit_points = hp_roll + int(con_mod)
        elif self.character_class == "Fighter":
            hp_roll = rolld10()
            max_hit_points = hp_roll + int(con_mod)
        else:
            max_hit_points = hp_roll + int(con_mod)

        #print("DEBUG")
        #print("class: %s" % character_class)
        #print("roll: %d" % hp_roll)
        #print("CON bonus: %d" % int(con_mod))
        if max_hit_points < 1:
            max_hit_points = 1

        return max_hit_points

    def update_sheet(self):
        # when changing character class - update things like HP and saving throw modifiers
        # Updating HP
        self.character_class = self.classSelectionBox.currentText()
        const_mod = int(self.statsTable.item(2,1).text())
        # print("DEBUG: HP mod = %d" % const_mod)
        updated_hit_points = int(self.generate_hit_points(self.character_class, const_mod))
        # print("DEBUG: updated HP: %s" % updated_hit_points)
        self.hitPointsLabel.setText(str(updated_hit_points))
        #Updating Saving throws:
        self.update_save_mods()

    def update_save_mods(self):
        # Updating Saving throws:
        self.save_modifiers = self.get_char_save_modifiers(
            self.character_class)
        self.savingThrowTable.setItem(0, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Strength"])))
        self.savingThrowTable.setItem(1, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Dexterity"])))
        self.savingThrowTable.setItem(2, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Constitution"])))
        self.savingThrowTable.setItem(3, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Intelligence"])))
        self.savingThrowTable.setItem(4, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Wisdom"])))
        self.savingThrowTable.setItem(5, 0, QtWidgets.QTableWidgetItem(
            str(self.save_modifiers["Charisma"])))

    def reroll_stats(self):
        for i in range(0, 6):
            # print(i) OK
            new_stat = get_character_stat(roll4xd6())
            self.statsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(
                str(new_stat)))
            self.statsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(
                self.get_stat_mod(new_stat)))
        # when re-rolling main stats - update Hit Points too
        const_mod = int(self.statsTable.item(2,1).text())
        new_hp = self.generate_hit_points(self.character_class, const_mod)
        self.hitPointsLabel.setText(str(new_hp))

        # when re-rolling stats update the Save Modifiers
        self.update_save_mods()

    def reroll_hp(self):
        con_mod = int(self.statsTable.item(2,1).text())
        new_hp = self.generate_hit_points(self.character_class, con_mod)
        self.hitPointsLabel.setText(str(new_hp))

    def get_stat_mod(self, stat):
        stat_mod = 0
        if stat == 1:
            stat_mod = "-5"
        elif stat in [2, 3]:
            stat_mod = "-4"
        elif stat in [4, 5]:
            stat_mod = "-3"
        elif stat in [6, 7]:
            stat_mod = "-2"
        elif stat in [8, 9]:
            stat_mod = "-1"
        elif stat in [10, 11]:
            stat_mod = "+0"
        elif stat in [12, 13]:
            stat_mod = "+1"
        elif stat in [14, 15]:
            stat_mod = "+2"
        elif stat in [16, 17]:
            stat_mod = "+3"
        elif stat in [18, 19]:
            stat_mod = "+4"
        return stat_mod

    def get_char_save_modifiers(self, char_class):
        class_prof_modifiers = {
            "Rogue": {
                "Strength": 0,
                "Dexterity": 2,
                "Constitution": 0,
                "Intelligence": 2,
                "Wisdom": 0,
                "Charisma": 0
            },
            "Wizard": {
                "Strength": 0,
                "Dexterity": 0,
                "Constitution": 0,
                "Intelligence": 2,
                "Wisdom": 2,
                "Charisma": 0
            },
            "Cleric": {
                "Strength": 0,
                "Dexterity": 0,
                "Constitution": 0,
                "Intelligence": 0,
                "Wisdom": 2,
                "Charisma": 2
            },
            "Fighter": {
                "Strength": 2,
                "Dexterity": 0,
                "Constitution": 2,
                "Intelligence": 0,
                "Wisdom": 0,
                "Charisma": 0
            }
        }
        char_save_profs = class_prof_modifiers[char_class]

        num_str_mod = int(self.statsTable.item(0,1).text()) + int(char_save_profs["Strength"])
        num_dex_mod = int(self.statsTable.item(1,1).text()) + int(char_save_profs["Dexterity"])
        num_con_mod = int(self.statsTable.item(2,1).text()) + int(char_save_profs["Constitution"])
        num_int_mod = int(self.statsTable.item(3,1).text()) + int(char_save_profs["Intelligence"])
        num_wis_mod = int(self.statsTable.item(4,1).text()) + int(char_save_profs["Wisdom"])
        num_cha_mod = int(self.statsTable.item(5,1).text()) + int(char_save_profs["Charisma"])

        if num_str_mod >= 0:
            txt_str_mod = "+" + str(num_str_mod)
        else:
            txt_str_mod = str(num_str_mod)

        if num_dex_mod >= 0:
            txt_dex_mod = "+" + str(num_dex_mod)
        else:
            txt_dex_mod = str(num_dex_mod)

        if num_con_mod >= 0:
            txt_con_mod = "+" + str(num_con_mod)
        else:
            txt_con_mod = str(num_con_mod)

        if num_int_mod >= 0:
            txt_int_mod = "+" + str(num_int_mod)
        else:
            txt_int_mod = str(num_int_mod)

        if num_wis_mod >= 0:
            txt_wis_mod = "+" + str(num_wis_mod)
        else:
            txt_wis_mod = str(num_wis_mod)

        if num_cha_mod >= 0:
            txt_cha_mod = "+" + str(num_cha_mod)
        else:
            txt_cha_mod = str(num_cha_mod)

        character_save_modifiers = {
            "Strength": txt_str_mod,
            "Dexterity": txt_dex_mod,
            "Constitution": txt_con_mod,
            "Intelligence": txt_int_mod,
            "Wisdom": txt_wis_mod,
            "Charisma": txt_cha_mod
        }

        return character_save_modifiers

    def set_character_name(self):
        self.character_name = self.characterNameEdit.text()

    def set_character_race(self):
        self.character_race = self.raceSelectionBox.currentText()

    def gerate_pdf_sheet(self):
        # template variables to be replaced by actual values:

        # if you didn't press ENTER in character name it will be empty.
        # workaround: assume UNNAMED_CHARACTER as file name

        if self.character_name == "":
            self.character_name = "UNNAMED_DUDE"

        context = {
            "character_class": self.character_class,
            "character_name": self.character_name,
            "character_race": self.character_race,
            "character_str": self.statsTable.item(0, 0).text(),
            "character_dex": self.statsTable.item(1, 0).text(),
            "character_con": self.statsTable.item(2, 0).text(),
            "character_int": self.statsTable.item(3, 0).text(),
            "character_wis": self.statsTable.item(4, 0).text(),
            "character_cha": self.statsTable.item(5, 0).text(),
            "str_mod": self.statsTable.item(0, 1).text(),
            "dex_mod": self.statsTable.item(1, 1).text(),
            "con_mod": self.statsTable.item(2, 1).text(),
            "int_mod": self.statsTable.item(3, 1).text(),
            "wis_mod": self.statsTable.item(4, 1).text(),
            "cha_mod": self.statsTable.item(5, 1).text(),
            "save_str_mod": self.savingThrowTable.item(0, 0).text(),
            "save_dex_mod": self.savingThrowTable.item(1, 0).text(),
            "save_con_mod": self.savingThrowTable.item(2, 0).text(),
            "save_int_mod": self.savingThrowTable.item(3, 0).text(),
            "save_wis_mod": self.savingThrowTable.item(4, 0).text(),
            "save_cha_mod": self.savingThrowTable.item(5, 0).text(),
            "character_max_hp": self.hitPointsLabel.text()
        }

        pdf_output_file_name = self.character_name + '.pdf'
        pdf_output_path = "character_sheets/" + pdf_output_file_name
        print("DEBUG: will output in: %s" % pdf_output_path)
        sheet_template_folder = "html_templates/"
        template_loader = jinja2.FileSystemLoader(sheet_template_folder)
        template_env = jinja2.Environment(loader=template_loader)

        template = template_env.get_template('character_sheet_template.html')
        output_text = template.render(context)

        #now export the pdf

        wkhtmltopdf_paths_per_os = {
            "Darwin": "/usr/local/bin/wkhtmltopdf",
            "Linux": "/usr/local/bin/wkhtmltopdf",
            "Windows": "C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        }
        os_platform = platform.system()

        wkhtmltopdf_binary = wkhtmltopdf_paths_per_os[os_platform]
        pdf_export_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_binary)
        pdfkit.from_string(output_text, pdf_output_path, configuration=pdf_export_config)

