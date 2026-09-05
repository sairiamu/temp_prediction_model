export function SkeuoToggle({ checked, onChange }: { checked: boolean; onChange: (checked: boolean) => void }) {
  return <label><input type="checkbox" checked={checked} onChange={(event) => onChange(event.target.checked)} /> Enabled</label>;
}
