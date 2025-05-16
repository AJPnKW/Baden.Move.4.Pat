# Baden Move for Pat

This is a personalized GitHub Pages web portal created to organize, document, and manage the move and renovation project for Pat and team.

## 🔐 Access

Visit the live site: [https://ajpnkw.github.io/Baden.Move.4.Pat/](https://ajpnkw.github.io/Baden.Move.4.Pat/)

Use one of the following codes to access the appropriate subsite:

| Code     | Subsite Redirect |
|----------|------------------|
| `wInStOn` | Winston's Dashboard |
| `tOdD`    | Todd's Dashboard    |
| `aLEx`    | Alex's Dashboard    |
| *invalid* | Redirects to [temu.com](https://temu.com) |

## 📁 Project Structure

```
Root/
├── index.html               → Secure landing page for access code entry
├── shared/styles.css        → Shared layout and Material Design styles
├── winston/                 → Winston’s full dashboard
│   ├── index.html
│   ├── todo.html
│   ├── projectplan.html
│   ├── design.html
│   ├── decisions.html
│   ├── gallery.html
│   └── admin.html
├── todd/                    → Todd’s full dashboard
│   └── same as Winston’s pages
├── alex/                    → Alex’s full dashboard
│   └── same as Winston’s pages
```

## 🎨 UI & Design

- Built with a modern Google/Material aesthetic using Roboto fonts
- Left-hand navigation sidebar on every subsite
- Responsive layout base for future mobile enhancement

## 🔧 Admin Access

Each subsite includes an `admin.html` page:

- **Login Password**: `bR@nT`
- Reveals metadata editor textarea (for future expansion)

## ✅ Features

- Secure code-based access routing
- Modular subsites for each user/group
- Visual navigation map and consistent structure
- Placeholder pages for to-do lists, decision tracking, gallery, etc.
- Validated JSON metadata support for file management (via hooks)

## 📦 How to Deploy

1. Unzip the contents to your GitHub local repo folder:
   `C:/Users/Lenovo/Projects.Github/Baden.Move.4.Pat`
2. Push using the provided PowerShell push script or GitHub Desktop
3. Ensure Pages settings in GitHub are set to:
   - **Branch**: `master`
   - **Folder**: `/ (root)`

## 🔮 Future Enhancements

- Editable and savable metadata per item (with JSON storage)
- Gallery viewer with filtering (date, tag, person)
- Task status tracking with drag-and-drop or checkbox logic
- Real-time decision/status updates
- Integration with Google Drive or OneDrive for storage sync

---

This project was designed for clarity, ease-of-use, and practical project communication. No programming background required to maintain or update.
