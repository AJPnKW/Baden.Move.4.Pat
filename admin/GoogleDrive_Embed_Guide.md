# Google Drive Embed Instructions for Baden.Move.4.Pat

These embeds are included in your site files and point to shared folders hosted in Google Drive.

## Current Mapped Folders

| Subsite | Page | Folder ID | Google Drive Link |
|--------|------|-----------|-------------------|
| alex | photos.html | 15B79sFlDyFQpK5GccHQr1MrZTDLGPJYm | https://drive.google.com/drive/folders/15B79sFlDyFQpK5GccHQr1MrZTDLGPJYm |
| todd | photos.html | 1-mQhKIXqDHMdObzT3wk2AuX0nYVCwt3J | https://drive.google.com/drive/folders/1-mQhKIXqDHMdObzT3wk2AuX0nYVCwt3J |
| baden | gallery.html | 1Aoz-62HJBlrcIpWxqpE0-wNukzWSxTFi | https://drive.google.com/drive/folders/1Aoz-62HJBlrcIpWxqpE0-wNukzWSxTFi |
| shared | admin/shared_resources.html | 1SO64X1upbgBGuz4tk8a0RKplpOo6LgHa | https://drive.google.com/drive/folders/1SO64X1upbgBGuz4tk8a0RKplpOo6LgHa |

## Embed Syntax Example (Used in site)

```html
<iframe
  src="https://drive.google.com/embeddedfolderview?id=FOLDER_ID#grid"
  width="100%"
  height="600"
  frameborder="0">
</iframe>
```

## Tips:
- You can replace FOLDER_ID with your folder value from Google Drive
- All folders must be shared with "Anyone with the link can view"
- You can customize the `#grid` to `#list` if you want a different layout
