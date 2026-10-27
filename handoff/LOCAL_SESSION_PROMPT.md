# Auftrag für eine lokale Claude-Session in /Users/christian/Work/Skills

Kopiere den Text unten in eine neue Claude-Code- oder Claude-App-Session, die im Ordner
`/Users/christian/Work/Skills` läuft. Lege vorher `skills-update.patch` in diesen Ordner.

---

Wende die Änderungen aus `skills-update.patch` auf die Skills in diesem Ordner an.

Hintergrund: Wir integrieren eine Interaktionsdesign-Methode (Jackson, Rosenberg, Prater,
Cooper, Norman, Shneiderman, Apple) als neuen Skill `interaction-model` und verdrahten ihn
mit den bestehenden Skills. Der Patch wurde gegen die auf claude.ai synchronisierten
Versionen erstellt, nicht gegen diesen Ordner.

Vorgehen:
1. Lies den Patch. Er betrifft:
   - neu: `interaction-model/` (SKILL.md, INSTALL.md, references/worksheets.md,
     references/sources.md)
   - geändert: `method-selector` (SKILL.md, references/method-map.md),
     `solution-architecture-lite`, `inacta-proposal-writing`, `clear-by-design`
   - geändert im V-Model-Paket: `vmodel-workflow`, `arc42-documentation`, `test-strategy`,
     die zwei `project-context.template.md` und die Plugin-Version auf 0.3.0
2. Die Pfade im Patch lauten `skills/<name>/...` und `plugins/inacta-vmodel/...`. Finde die
   passenden Ordner hier (das V-Model liegt vermutlich unter `vmodel/skills/` und
   `vmodel/platform/claude/`). Zeige mir die Zuordnung, bevor du etwas änderst.
3. Prüfe zuerst mit `git apply --check` (Pfade per `--directory` oder angepasster Kopie
   umgemappt). Wenn ein Hunk nicht passt, weil die lokale Version neuer ist, übertrage die
   Änderung sinngemäss von Hand und nenne mir die Stelle.
4. Prüfe danach: jede `description` hat höchstens 1024 Zeichen, keine Gedankenstriche
   (em-dash), deutsche Texte mit echten Umlauten und ss statt ß.
5. Committe in diesem Ordner, falls er ein Git-Repository ist.
6. Danach frag mich, ob du die geänderten Skills und das V-Model-Plugin in die Organisation
   publizieren sollst. Publiziere erst nach meinem Ja und ersetze bestehende Uploads nur
   nach Rückfrage.
