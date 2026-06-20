import FileEditor from "../components/file/FileEditor";

import Timeline from "../components/continuity/Timeline";
import LineagePanel from "../components/continuity/LineagePanel";
import ReceiptsPanel from "../components/continuity/ReceiptsPanel";

export default function NovaCodingAgent() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Nova Continuity Cockpit</h1>

      <FileControls />
      <FileEditor />

      <hr />

      <Timeline />
      <LineagePanel />
      <ReceiptsPanel />
    </div>
  );
}
