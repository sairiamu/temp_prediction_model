import classification from "../mocks/mockClassification.json";
import { ClassificationPanel } from "../components/panels/ClassificationPanel";
import type { ClassificationResult } from "../types";
export function Classification() { return <ClassificationPanel result={classification as ClassificationResult} />; }
