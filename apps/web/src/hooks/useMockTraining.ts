import { useState } from "react";
export function useMockTraining() { const [isTraining, setIsTraining] = useState(false); return { isTraining, start: () => setIsTraining(true), stop: () => setIsTraining(false) }; }
