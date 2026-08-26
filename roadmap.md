# FERA 2.0 — Project Roadmap

> Single source of truth for project execution.
> Update this file whenever a numbered step is completed.
>
> Status:
> - `[x]` Complete
> - `[~]` In progress
> - `[ ]` Pending

---

## Phase 1 — Project Foundation

### Step 1 — Project Architecture
- [x] Establish backend application structure
- [x] Establish configuration/contracts
- [x] Establish testing structure
- [x] Establish health/service foundations

### Step 2 — Dataset Contracts
- [x] Define dataset metadata contract
- [x] Define VED data-source contract
- [x] Add contract tests

### Step 3 — VED Dataset Discovery
- [x] Locate VED raw archives
- [x] Inspect archive structure
- [x] Verify Part 1 / Part 2 weekly files
- [x] Verify VED fuel-rate availability
- [x] Verify feature availability
- [x] Verify vehicle/trip coverage

---

## Phase 2 — VED Data Pipeline

### Step 4 — VED Record Mapping
- [x] Define normalized VED fuel record
- [x] Map raw VED fields to internal schema
- [x] Validate normalized records
- [x] Add mapper tests

### Step 5 — VED Archive Reader
- [x] Implement 7z archive reader
- [x] Read weekly CSV members
- [x] Skip missing fuel-rate rows
- [x] Handle streaming record generation
- [x] Add reader tests

### Step 6 — VED Batch Preprocessing
- [x] Discover weekly archive members
- [x] Process Part 1 and Part 2 archives
- [x] Write normalized processed CSV files
- [x] Add manifest generation
- [x] Validate processed dataset
- [x] Process all 54 weekly files
- [x] Verify 896,097 processed records
- [x] Verify no bad/empty processed files
- [x] Add batch preprocessing tests

---

## Phase 3 — ML Dataset

### Step 7 — ML Dataset Definition
- [x] Define ML record contract
- [x] Create processed-data loader
- [x] Define ML features
- [x] Define prediction target
- [x] Build feature/target matrix
- [x] Handle missing optional telemetry
- [x] Build ML preparation pipeline
- [x] Support multi-file dataset loading
- [x] Validate against real VED data
- [x] Verify 896,097 rows / 7 features / 0 missing values

---

## Phase 4 — Evaluation & Baselines

### Step 8 — Evaluation Strategy
- [x] Define vehicle-grouped train/test split
- [x] Create split contract
- [x] Validate vehicle leakage prevention
- [x] Validate split against real VED data

### Step 9 — Baseline Models
- [x] Implement Random Forest baseline
- [x] Implement regression evaluation metrics
- [x] Benchmark Random Forest on real VED
- [x] Implement mean/naive baseline
- [x] Compare naive baseline vs Random Forest
- [x] Establish initial model benchmark

### Step 10 — Error Analysis
- [x] Analyze error by fuel-rate range
- [x] Run real VED error analysis
- [x] Implement prediction-bias analysis
- [x] Analyze baseline prediction bias
- [x] Document baseline weaknesses

---

## Phase 5 — Model Improvement

### Step 11 — Ridge Efficiency Model
- [x] Implement Ridge regression model
- [x] Compare Ridge vs Random Forest
- [x] Analyze Ridge bias
- [x] Analyze Ridge errors by fuel-rate range
- [x] Inspect Ridge feature coefficients
- [x] Add multi-file ML preparation
- [x] Evaluate Ridge on full processed VED
- [x] Evaluate performance per held-out vehicle
- [x] Analyze held-out vehicle composition
- [x] Record official Ridge benchmark

### Current Official Benchmark

| Model | MAE (L/hr) | RMSE (L/hr) | R² |
|---|---:|---:|---:|
| Ridge | 0.279842 | 0.659426 | 0.842988 |

Dataset:
- 896,097 processed records
- 13 vehicles with fuel-rate data
- Vehicle-grouped evaluation
- 10 training vehicles
- 3 held-out vehicles

---

## Phase 6 — Feature Engineering

### Step 12 — Feature Engineering
- [ ] Define physically meaningful derived features
- [ ] Add speed/power/engine interaction features
- [ ] Add temporal/trip features where justified
- [ ] Evaluate feature distributions
- [ ] Test feature usefulness
- [ ] Compare engineered Ridge against Step 11 benchmark
- [ ] Reject features that do not improve generalization

### Step 13 — Feature Selection
- [ ] Analyze feature importance / coefficients
- [ ] Identify redundant features
- [ ] Test reduced feature sets
- [ ] Select final feature set
- [ ] Lock feature contract

---

## Phase 7 — Model Development

### Step 14 — Candidate Model Comparison
- [ ] Establish candidate model interface
- [ ] Evaluate Ridge
- [ ] Evaluate tree-based regression
- [ ] Evaluate gradient-boosting model
- [ ] Compare all candidates using identical splits
- [ ] Select strongest candidate

### Step 15 — Hyperparameter Optimization
- [ ] Define bounded search space
- [ ] Use vehicle-grouped validation
- [ ] Tune selected model
- [ ] Compare tuned model against Step 11 benchmark
- [ ] Prevent test-set tuning leakage
- [ ] Lock final hyperparameters

### Step 16 — Final Model Evaluation
- [x] Run final held-out evaluation
- [x] Calculate MAE
- [x] Calculate RMSE
- [ ] Calculate R²
- [x] Analyze per-vehicle performance
- [x] Analyze fuel-rate ranges
- [x] Analyze prediction bias
- [x] Establish final model benchmark

---

## Phase 8 — Production ML Pipeline

### Step 17 — Training Pipeline
- [x] Build reproducible training pipeline
- [ ] Load processed VED dataset
- [ ] Apply locked feature transformations
- [ ] Apply locked train/test grouping
- [ ] Train final model
- [x] Save model artifact
- [x] Save feature metadata
- [x] Save evaluation metadata

### Step 18 — Model Artifact Management
- [ ] Define model artifact contract
- [ ] Define model version
- [ ] Store training metadata
- [ ] Store feature schema
- [ ] Store evaluation metrics
- [ ] Add artifact loading tests

### Step 19 — Prediction Service
- [ ] Define prediction request contract
- [ ] Define prediction response contract
- [ ] Load trained model
- [ ] Apply identical feature transformations
- [ ] Generate fuel-rate prediction
- [ ] Validate prediction inputs
- [ ] Add service tests

---

## Phase 9 — Backend Integration

### Step 20 — Efficiency Service
- [ ] Integrate prediction service with backend
- [ ] Add efficiency calculation endpoints
- [ ] Add validation/error handling
- [ ] Add service-level tests

### Step 21 — API Layer
- [ ] Define API routes
- [ ] Define request/response schemas
- [ ] Connect routes to efficiency service
- [ ] Add API tests
- [ ] Verify health/config/data endpoints

### Step 22 — Backend Integration Testing
- [ ] Test complete request ? prediction flow
- [ ] Test invalid inputs
- [ ] Test missing telemetry
- [ ] Test model loading failures
- [ ] Test API responses

---

## Phase 10 — Frontend / Product Layer

### Step 23 — Dashboard Foundation
- [ ] Define dashboard information architecture
- [ ] Connect frontend to backend API
- [ ] Display vehicle data
- [ ] Display efficiency metrics
- [ ] Display prediction results

### Step 24 — Efficiency Visualization
- [ ] Fuel-rate visualization
- [ ] Efficiency trends
- [ ] Vehicle comparison
- [ ] Trip-level analysis
- [ ] Prediction vs actual visualization
- [ ] Error visualization

### Step 25 — User Experience
- [ ] Loading states
- [ ] Error states
- [ ] Empty states
- [ ] Input validation
- [ ] Responsive layout
- [ ] Final UI polish

---

## Phase 11 — Reliability & Production Readiness

### Step 26 — Testing
- [ ] Run complete backend test suite
- [ ] Add integration tests
- [ ] Add model regression tests
- [ ] Add API tests
- [ ] Add frontend tests where applicable

### Step 27 — Data & Model Validation
- [ ] Validate processed-data manifest
- [ ] Validate feature schema
- [ ] Validate model artifact
- [ ] Validate prediction ranges
- [ ] Validate model performance against locked benchmark

### Step 28 — Performance
- [ ] Measure preprocessing performance
- [ ] Measure training performance
- [ ] Measure prediction latency
- [ ] Optimize bottlenecks
- [ ] Verify memory usage

### Step 29 — Security & Configuration
- [ ] Review configuration handling
- [ ] Review secrets/environment variables
- [ ] Validate API inputs
- [ ] Review filesystem access
- [ ] Review production error handling

---

## Phase 12 — Deployment

### Step 30 — Deployment Preparation
- [ ] Define production configuration
- [ ] Prepare deployment artifacts
- [ ] Prepare model artifact
- [ ] Prepare processed-data requirements
- [ ] Document startup procedure

### Step 31 — Deployment
- [ ] Deploy backend
- [ ] Deploy frontend
- [ ] Connect production services
- [ ] Verify health checks
- [ ] Verify prediction endpoint

### Step 32 — Production Validation
- [ ] Run smoke tests
- [ ] Verify real prediction flow
- [ ] Verify error handling
- [ ] Verify logs
- [ ] Verify performance

---

## Phase 13 — Finalization

### Step 33 — Documentation
- [ ] Architecture documentation
- [ ] Data pipeline documentation
- [ ] ML methodology documentation
- [ ] API documentation
- [ ] Deployment documentation
- [ ] Usage instructions

### Step 34 — Final QA
- [ ] Full test suite passes
- [ ] No known critical bugs
- [ ] Model benchmark recorded
- [ ] Data pipeline reproducible
- [ ] Production flow verified

### Step 35 — Project Release
- [ ] Final cleanup
- [ ] Final git status clean
- [ ] Final release commit/tag
- [ ] Final project review
- [ ] FERA 2.0 release

---

# Execution Rules

1. Work in numbered steps.
2. Complete and verify the current step before moving forward.
3. Run targeted tests during development.
4. Run the full test suite at major checkpoints.
5. Never tune against the held-out test vehicles.
6. Keep vehicle leakage out of evaluation.
7. Record important benchmarks here.
8. Commit completed milestones.
9. Do not repeat inspections unless new evidence requires them.
10. Prefer execution over unnecessary explanation.
11. If a test fails, fix the failure before advancing.
12. If the architecture is uncertain, inspect the existing code before modifying it.

---

## Current Position

**Completed through Step 11.**

**Next:** Step 12 — Feature Engineering

**Current best benchmark:** Ridge  
**MAE:** 0.279842 L/hr  
**RMSE:** 0.659426 L/hr  
**R²:** 0.842988

