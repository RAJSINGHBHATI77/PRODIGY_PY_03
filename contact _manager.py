import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("👤 Name: ")
    phone = input("📞 Phone: ")
    email = input("📧 Email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"✅ Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"👤 {name} | 📞 {info['Phone']} | 📧 {info['Email']}")

def edit_contact(contacts):
    name = input("🔍 Enter name to edit: ")
    if name in contacts:
        phone = input("📞 New Phone: ")
        email = input("📧 New Email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"📝 Contact '{name}' updated.")
    else:
        print("❌ Contact not found.")

def delete_contact(contacts):
    name = input("🗑️ Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n📒 Contact Manager Menu:")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Edit Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("💾 Contacts saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

main()
