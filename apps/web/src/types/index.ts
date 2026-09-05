export type PageKey = "dashboard" | "upload" | "forecast" | "anomalies" | "classification";

export interface ForecastPoint {
  timestamp: string;
  actual?: number;
  predicted: number;
  lower?: number;
  upper?: number;
}

export interface LossPoint {
  epoch: number;
  train: number;
  validation: number;
}

export interface AnomalyPoint {
  timestamp: string;
  value: number;
  score: number;
  isAnomaly: boolean;
}

export interface ClassificationResult {
  regime: string;
  confidence: number;
  signals: string[];
}
